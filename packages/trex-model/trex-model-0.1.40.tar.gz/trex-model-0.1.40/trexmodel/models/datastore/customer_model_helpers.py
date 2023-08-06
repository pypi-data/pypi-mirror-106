'''
Created on 29 Apr 2021

@author: jacklok
'''
from trexlib.utils.string_util import is_empty, is_not_empty
from datetime import datetime


def update_reward_summary_with_new_reward(existing_reward_summary, reward_details):
    reward_summary              = existing_reward_summary
    reward_format               = reward_details.get('reward_format')
    reward_amount               = reward_details.get('reward_amount')
    used_reward_amount          = reward_details.get('used_reward_amount')
    latest_expiry_date          = datetime.strptime(reward_details.get('expiry_date'), '%d-%m-%Y').date()
    
    
    existing_latest_expiry_date = None
    new_latest_expiry_date      = latest_expiry_date
    
    if is_empty(reward_summary):
        reward_balance = reward_amount - used_reward_amount
        reward_summary = {
                            reward_format:{
                                            'latest_expiry_date'    : new_latest_expiry_date.strftime('%d-%m-%Y'),
                                            'amount'                : reward_amount
                                            }
                                        
                            }
    else:
        reward_summary_by_reward_format = reward_summary.get(reward_format)
        
        if reward_summary_by_reward_format is None:
            reward_summary_by_reward_format = {
                                                'amount': 0,
                                                }
            new_latest_expiry_date = latest_expiry_date
        else:
        
            existing_latest_expiry_date = reward_summary_by_reward_format.get('latest_expiry_date')
            existing_latest_expiry_date = latest_expiry_date
            
            if latest_expiry_date > existing_latest_expiry_date:  
                new_latest_expiry_date = existing_latest_expiry_date
                
                
        
        reward_summary_by_reward_format['latest_expiry_date']   = new_latest_expiry_date.strftime('%d-%m-%Y')
        
        reward_balance = reward_amount - used_reward_amount
        
        reward_summary_by_reward_format['amount']               = reward_summary_by_reward_format['amount'] + reward_balance
        
        reward_summary[reward_format] = reward_summary_by_reward_format
        
    return reward_summary

def update_reward_summary_with_reverted_reward(existing_reward_summary, reward_details):
    reward_summary              = existing_reward_summary
    reward_format               = reward_details.get('reward_format')
    reward_amount               = reward_details.get('reward_amount')
    
    existing_latest_expiry_date = None
    
    if is_not_empty(reward_summary):
        reward_summary_by_reward_format = reward_summary.get(reward_format)
        
        existing_latest_expiry_date = reward_summary_by_reward_format.get('latest_expiry_date')
        existing_latest_expiry_date = datetime.strptime(existing_latest_expiry_date, '%d-%m-%Y').date()
        
        final_reward_amount                         = reward_summary_by_reward_format['amount'] - reward_amount
        reward_summary_by_reward_format['amount']   = final_reward_amount
        reward_summary[reward_format]               = reward_summary_by_reward_format
        
        if final_reward_amount==0:
            del reward_summary[reward_format]
        
    return reward_summary
