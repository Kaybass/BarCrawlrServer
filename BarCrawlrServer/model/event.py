from enum import Enum, auto



class eventCodes(Enum):

    #Success log codes
    successful_update = auto()
    successful_plan_creation = auto()
    successful_user_addition = auto()
    successful_user_deletion = auto()
    successful_plan_deletion = auto()

    #Error log codes
    error_four_oh_four = auto()
    error_bad_api_key = auto()
    error_bad_username = auto()
    error_bad_plan_id = auto()

"""
 Events need to be given ip addresses like (events[code] + request.environ['REMOTE_ADDR'])
"""
events = {
    #Success log codes
    eventCodes.successful_update : 'User successfully updated info from ip: '
    ,eventCodes.successful_plan_creation : 'User successfully added plan from ip: '
    ,eventCodes.successful_user_addition : 'User successfully added info from ip: '
    ,eventCodes.successful_user_deletion : 'User successfully deleted info from ip: '
    ,eventCodes.successful_plan_deletion : 'User successfully deleted plan from ip: '

    #Error log codes
    ,eventCodes.error_four_oh_four : '404 error from ip: '
    ,eventCodes.error_bad_api_key : 'Bad api key from ip: '
    ,eventCodes.error_bad_username : 'Bad username from ip: '
    ,eventCodes.error_bad_plan_id : 'Bad plan name from ip: '
}

eventsTypes = {
    #Success log codes
    eventCodes.successful_update : 'Update'
    ,eventCodes.successful_plan_creation : 'Plan Create'
    ,eventCodes.successful_user_addition : 'User Add'
    ,eventCodes.successful_user_deletion : 'User Delete'
    ,eventCodes.successful_plan_deletion : 'Plan Delete'

    #Error log codes
    ,eventCodes.error_four_oh_four : 'Error 404'
    ,eventCodes.error_bad_api_key : 'Error api key'
    ,eventCodes.error_bad_username : 'Error user id'
    ,eventCodes.error_bad_plan_id : 'Error plan id'
}


class event(object):
    
    def __init__(self, eventType, eventMessage):
        
        self.eventType = eventType
        self.eventMessage = eventMessage

    def toString(self):
        return '"' + eventType + '": ' + eventMessage


