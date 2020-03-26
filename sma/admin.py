from django.contrib import admin
from .models import School,Grade,Student,Mentor,Student_Group_Mentor_Assignment,Session_Schedule,Attendance,User

# Register your models here.
class SchoolList(admin.ModelAdmin):
    list_display = ('school_name', 'school_email', 'school_phone')
    list_filter = ('school_name', 'school_email')
    search_fields = ('school_name',)
    ordering = ['school_name']

class GradeList(admin.ModelAdmin):
    list_display = ['grade_num']
    list_filter = ['grade_num']
    search_fields = ['grade_num']
    ordering = ['grade_num']

class StudentList(admin.ModelAdmin):
    list_display = ('student_first_name','student_middle_name', 'student_last_name','school','grade')
    list_filter = ('student_first_name', 'student_last_name','school','grade')
    search_fields = ('student_first_name', 'student_last_name','school','grade')
    ordering = ['student_first_name']

class MentorList(admin.ModelAdmin):
    list_display = ('mentor_first_name','mentor_middle_name', 'mentor_last_name','mentor_email','mentor_phone')
    list_filter = ('mentor_first_name','mentor_middle_name', 'mentor_last_name','mentor_email','mentor_phone')
    search_fields = ('mentor_first_name','mentor_middle_name', 'mentor_last_name','mentor_email','mentor_phone')
    ordering = ['mentor_first_name']

class GroupMentorAssignmentList(admin.ModelAdmin):
    list_display = ('group_name','school','grade','mentor')
    list_filter = ('group_name','school','grade','mentor')
    search_fields = ('group_name','school','grade','mentor')
    ordering = ['group_name']

class SessionScheduleList(admin.ModelAdmin):
    list_display = ('session_name','session_location','mentor','group','session_start_date','session_end_date')
    list_filter = ('session_name','session_location','mentor','group','session_start_date','session_end_date')
    search_fields = ('session_name','session_location','mentor','group','session_start_date','session_end_date')
    ordering = ['session_name']

class AttendanceList(admin.ModelAdmin):
    list_display = ('attendance_student_id','attendance_grade_id','attendance_mentor_id','attendance_session_ID','attendance_ID')
    list_filter = ('attendance_student_id','attendance_grade_id','attendance_mentor_id','attendance_session_ID','attendance_ID')
    search_fields = ('attendance_student_id','attendance_grade_id','attendance_mentor_id','attendance_session_ID','attendance_ID')
    ordering = ['attendance_session_ID']

class UserList(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'email','username','is_active','created_on','role','is_staff','is_member')
    list_filter = ('first_name','last_name', 'email','username','is_active','created_on','role','is_staff','is_member')
    search_fields = ('first_name','last_name', 'email','username','is_active','created_on','role','is_staff','is_member')
    ordering = ['first_name']


admin.site.register(School,SchoolList)
admin.site.register(Grade,GradeList)
admin.site.register(Student,StudentList)
admin.site.register(Mentor,MentorList)
admin.site.register(Student_Group_Mentor_Assignment,GroupMentorAssignmentList)
admin.site.register(Session_Schedule,SessionScheduleList)
admin.site.register(Attendance,AttendanceList)
admin.site.register(User,UserList)




