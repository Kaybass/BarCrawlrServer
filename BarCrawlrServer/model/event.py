from enum import Enum#, auto

class eventCodes(Enum):

    #Success log codes
    successful_update = 0#auto()
    successful_plan_creation = 1#auto()
    successful_user_addition = 2#auto()
    successful_user_deletion = 3#auto()
    successful_plan_deletion = 4#auto()

    #Error log codes
    error_four_oh_four = 5#auto()
    error_bad_api_key = 6#auto()
    error_bad_username = 7#auto()
    error_bad_plan_id = 8#auto()

"""
 Events need to be given ip addresses like (events[code].format(request.environ['REMOTE_ADDR'])

 Event objects get initialized like event(eventTypes[eventCodes.code], events[eventCodes.code].format(request.environ['REMOTE_ADDR']))

 long I know but idc
"""
events = {
    #Success log codes
    eventCodes.successful_update : 'User successfully updated info from ip: {0}'
    ,eventCodes.successful_plan_creation : 'User successfully added plan from ip: {0}'
    ,eventCodes.successful_user_addition : 'User successfully added info from ip: {0}'
    ,eventCodes.successful_user_deletion : 'User successfully deleted info from ip: {0}'
    ,eventCodes.successful_plan_deletion : 'User successfully deleted plan from ip: {0}'

    #Error log codes
    ,eventCodes.error_four_oh_four : '404 error from ip: {0}'
    ,eventCodes.error_bad_api_key : 'Bad api key from ip: {0}'
    ,eventCodes.error_bad_username : 'Bad username from ip: {0}'
    ,eventCodes.error_bad_plan_id : 'Bad plan name from ip: {0}'
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
        return '"' + self.eventType + '": ' + self.eventMessage


