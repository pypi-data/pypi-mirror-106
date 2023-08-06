'''
Created on 26 Jan 2021

@author: jacklok
'''
from trexanalytics.conf import UPSTREAM_UPDATED_DATETIME_FIELD_NAME, MERCHANT_DATASET, SYSTEM_DATASET
import uuid, logging
from trexmodel.models.datastore.analytic_models import UpstreamData
from trexanalytics.bigquery_table_template_config import REGISTERED_CUSTOMER_TEMPLATE, REGISTERED_MERCHANT_TEMPLATE, MERCHANT_REGISTERED_CUSTOMER_TEMPLATE,\
    CUSTOMER_TRANSACTION_TEMPLATE, MERCHANT_CUSTOMER_REWARD_TEMPLATE 
from trexlib.utils.google.bigquery_util import default_serializable
from datetime import datetime, timedelta
from trexmodel.models.datastore.transaction_models import CustomerTransactionWithRewardDetails
from trexanalytics import conf
from trexmodel.models.datastore.ndb_models import convert_to_serializable_value

__REGISTERED_MERCHANT_TEMPLATE_UPSTREAM_SCHEMA = { 
                                                'MerchantKey'           : 'key_in_str',
                                                'CompanyName'           : 'company_name',
                                                'RegisteredDateTime'    : 'registered_datetime',
                                            }

__REGISTERED_CUSTOMER_TEMPLATE_UPSTREAM_SCHEMA = {
                                                'UserKey'           : 'registered_user_acct_key',
                                                'CustomerKey'       : 'key_in_str',
                                                'MerchantKey'       : 'registered_merchant_acct_key',
                                                'DOB'               : 'birth_date',
                                                'Gender'            : 'gender',
                                                'MobilePhone'       : 'mobile_phone',
                                                'Email'             : 'email',
                                                'MobileAppInstall'  : 'mobile_app_installed',
                                                'RegisteredDateTime': 'registered_datetime',
                                                'RegisteredOutlet'  : 'registered_outlet_key',
                                                }

__MERCHANT_REGISTERED_CUSTOMER_TEMPLATE_UPSTREAM_SCHEMA = {
                                                        'UserKey'           : 'registered_user_acct_key',
                                                        'CustomerKey'       : 'key_in_str',
                                                        'DOB'               : 'birth_date',
                                                        'Gender'            : 'gender',
                                                        'MobilePhone'       : 'mobile_phone',
                                                        'Email'             : 'email',
                                                        'MobileAppInstall'  : 'mobile_app_installed',
                                                        'RegisteredDateTime': 'registered_datetime',
                                                        'RegisteredOutlet'  : 'registered_outlet_key',
                                                        }


__CUSTOMER_TRANSACTION_DATA_TEMPLATE_UPSTREAM_SCHEMA = {
                                            "UserKey"               : 'transact_user_acct_key',
                                            "CustomerKey"           : 'transact_customer_key',
                                            "MerchantKey"           : 'transact_merchant_acct_key',
                                            "TransactOutlet"        : 'transact_outlet_key',
                                            "TransactionId"         : 'transaction_id',
                                            "InvoiceId"             : 'invoice_id',
                                            "TransactAmount"        : 'transact_amount',
                                            "TransactDateTime"      : 'transact_datetime',
                                            "Reverted"              : 'is_revert',
                                            "RevertedDateTime"      : 'reverted_datetime',
                                            }

__CUSTOMER_REWARD_DATA_TEMPLATE_UPSTREAM_SCHEMA = {
                                            "CustomerKey"           : 'transact_customer_key',
                                            "MerchantKey"           : 'transact_merchant_acct_key',
                                            "TransactOutlet"        : 'transact_outlet_key',
                                            "TransactionId"         : 'transaction_id',
                                            "TransactAmount"        : 'transact_amount',
                                            "TransactDateTime"      : 'transact_datetime',
                                            "RewardFormat"          : 'reward_format',
                                            "RewardAmount"          : 'reward_amount',
                                            "ExpiryDate"            : 'expiry_date',
                                            "RewardFormatKey"       : 'reward_format_key',
                                            "RewardedDateTime"      : 'rewarded_datetime',
                                            "Reverted"              : 'is_revert',
                                            "RevertedDateTime"      : 'reverted_datetime',
                                            }


upstream_schema_config = {
                            REGISTERED_MERCHANT_TEMPLATE            : __REGISTERED_MERCHANT_TEMPLATE_UPSTREAM_SCHEMA,
                            REGISTERED_CUSTOMER_TEMPLATE            : __REGISTERED_CUSTOMER_TEMPLATE_UPSTREAM_SCHEMA,
                            MERCHANT_REGISTERED_CUSTOMER_TEMPLATE   : __MERCHANT_REGISTERED_CUSTOMER_TEMPLATE_UPSTREAM_SCHEMA,
                            CUSTOMER_TRANSACTION_TEMPLATE           : __CUSTOMER_TRANSACTION_DATA_TEMPLATE_UPSTREAM_SCHEMA,
                            MERCHANT_CUSTOMER_REWARD_TEMPLATE       : __CUSTOMER_REWARD_DATA_TEMPLATE_UPSTREAM_SCHEMA,
                            }

logger = logging.getLogger('upstream')

def __create_upstream(upstream_entity, upstream_template, dataset_name, table_name, update_datetime=None, **kwargs):
    upstream_json = {}
    if upstream_entity:
        schema = upstream_schema_config.get(upstream_template)
        for upstrem_field_name, attr_name in schema.items():
            upstream_json[upstrem_field_name] = default_serializable(getattr(upstream_entity, attr_name))
    
    if update_datetime is None:
        update_datetime = datetime.now() - timedelta(hours=int(conf.SERVER_DATETIME_GMT))
            
    upstream_json['Key'] = uuid.uuid1().hex
    upstream_json[UPSTREAM_UPDATED_DATETIME_FIELD_NAME] = default_serializable(update_datetime)
    
    for key, value in kwargs.items():
        upstream_json[key] = convert_to_serializable_value(value)
    
    logger.debug('-------------------------------------------------')
    logger.debug('upstream_json=%s', upstream_json)
    logger.debug('-------------------------------------------------')
    UpstreamData.create(dataset_name, table_name, upstream_template, [upstream_json])
    

def create_registered_customer_upstream_for_system(customer):
    update_datetime     = datetime.now() - timedelta(hours=int(conf.SERVER_DATETIME_GMT))
    
    table_name          = REGISTERED_CUSTOMER_TEMPLATE
    final_table_name    = '{}_{}'.format(table_name, update_datetime.strftime('%Y%m%d'))
    
    __create_upstream(customer, REGISTERED_CUSTOMER_TEMPLATE, SYSTEM_DATASET, final_table_name, update_datetime=update_datetime)
    
def create_merchant_registered_customer_upstream_for_merchant(customer):
    update_datetime     = datetime.now() - timedelta(hours=int(conf.SERVER_DATETIME_GMT))
    
    table_name          = MERCHANT_REGISTERED_CUSTOMER_TEMPLATE
    merchant_acct       = customer.registered_merchant_acct
    account_code        = merchant_acct.account_code.replace('-','')
    final_table_name    = '{}_{}_{}'.format(table_name, account_code, update_datetime.strftime('%Y%m%d'))
    
    __create_upstream(customer, MERCHANT_REGISTERED_CUSTOMER_TEMPLATE, MERCHANT_DATASET, final_table_name, update_datetime=update_datetime)    
    
def create_merchant_customer_transaction_upstream_for_merchant(transaction_details, update_datetime=None):
    if update_datetime is None:
        update_datetime     = transaction_details.transact_datetime
        
    table_name          = CUSTOMER_TRANSACTION_TEMPLATE
    merchant_acct       = transaction_details.transact_merchant_acct
    account_code        = merchant_acct.account_code.replace('-','')
    final_table_name    = '{}_{}_{}'.format(table_name, account_code, update_datetime.strftime('%Y%m%d'))
    
    __create_upstream(transaction_details, CUSTOMER_TRANSACTION_TEMPLATE, MERCHANT_DATASET, final_table_name, 
                      update_datetime=update_datetime, Reverted=False, RevertedDateTime=None)
    
def create_merchant_customer_transaction_reveted_upstream_for_merchant(transaction_details, reverted_datetime, update_datetime=None):
    if update_datetime is None:
        update_datetime     = transaction_details.transact_datetime
        
    table_name          = CUSTOMER_TRANSACTION_TEMPLATE
    merchant_acct       = transaction_details.transact_merchant_acct
    account_code        = merchant_acct.account_code.replace('-','')
    final_table_name    = '{}_{}_{}'.format(table_name, account_code, update_datetime.strftime('%Y%m%d'))
    
    __create_upstream(transaction_details, CUSTOMER_TRANSACTION_TEMPLATE, MERCHANT_DATASET, final_table_name, 
                      update_datetime=update_datetime, Reverted=True, RevertedDateTime=reverted_datetime)    

def create_merchant_customer_reward_upstream_for_merchant(transaction_details, reward_details, update_datetime=None):
    if update_datetime is None:
        update_datetime     = datetime.now() - timedelta(hours=int(conf.SERVER_DATETIME_GMT))
    
    table_name          = MERCHANT_CUSTOMER_REWARD_TEMPLATE
    merchant_acct       = transaction_details.transact_merchant_acct
    account_code        = merchant_acct.account_code.replace('-','')
    final_table_name    = '{}_{}_{}'.format(table_name, account_code, update_datetime.strftime('%Y%m%d'))
    
    transaction_details_with_reward_details = CustomerTransactionWithRewardDetails(transaction_details, reward_details)
    
    __create_upstream(transaction_details_with_reward_details, MERCHANT_CUSTOMER_REWARD_TEMPLATE, MERCHANT_DATASET, final_table_name, 
                      update_datetime=update_datetime, Reverted=False, RevertedDateTime=None)
    
def create_merchant_customer_reward_reverted_upstream_for_merchant(transaction_details, reward_details, reverted_datetime, update_datetime=None):
    if update_datetime is None:
        update_datetime     = transaction_details.transact_datetime
    
    
    table_name          = MERCHANT_CUSTOMER_REWARD_TEMPLATE
    merchant_acct       = transaction_details.transact_merchant_acct
    account_code        = merchant_acct.account_code.replace('-','')
    final_table_name    = '{}_{}_{}'.format(table_name, account_code, update_datetime.strftime('%Y%m%d'))
    
    transaction_details_with_reward_details = CustomerTransactionWithRewardDetails(transaction_details, reward_details)
    
    __create_upstream(transaction_details_with_reward_details, MERCHANT_CUSTOMER_REWARD_TEMPLATE, MERCHANT_DATASET, final_table_name, 
                      update_datetime=update_datetime, Reverted=True, RevertedDateTime=reverted_datetime)    



