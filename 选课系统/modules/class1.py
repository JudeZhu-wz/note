class Class(object):
    '''
    班级类
    '''
    def __init__(self, class_name, course_obj):
        self.class_name = class_name
        self.class_course = course_obj
        self.class_student = {}