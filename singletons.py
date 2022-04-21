class TablePage:
    table = 'none'
    page = 1
    page_max = 1

class ViewTable:
    pass

class Box:
    ul_corner = '\u250c'
    ur_corner = '\u2510'
    bl_corner = '\u2514'
    br_corner = '\u2518'
    vertical_pipe = '\u2502'
    horizontal_pipe = '\u2500'
    horiz_verti_connector = '\u252c'
    
class MenuChoices:
    manager_main_menu = ''
    user_main_menu = ''


class UserLoggedIn:
    user_id = ''
    password = ''
    user_type = ''


class CurrentUser:
    user_id = ''
    first_name = ''
    last_name = ''
    phone = ''
    email = ''
    password = ''
    date_created = ''
    hire_date = ''
    user_type = ''
    active = ''
    object = 0
    
    
class CurrentObject:
    object = 0



class CompetencyLevels:
    user_id = ''
    first_name = ''
    last_name = ''
    email = ''
    competencies_dict = {}
    # competencies_dict = {
    #     'competency_1_name':{
    #         'assessment_1_name':['scores'],
    #         'assessment_2_name':['scores']
    #     },
    #     'competency_2_name':{
    #         'assessment_1_name':['scores'],
    #         'assessment_2_name':['scores']
    #     }
    # }
    
    
class CurrentCompetency:
    competency_id = 0
    name = ''
    description = None
    active = 0

class CurrentAssessment:
    assessment_id = 0
    competency_id = 0
    name = ''
    date_created = ''
    active = 0
    

class CurrentResult:
    results_id = 0
    user_id = 0
    assessment_id = 0
    score = ''
    date_taken = ''
    manager_id = 0
    active = 0
    
