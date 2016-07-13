from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.


class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 2

class ChoiceInline(admin.TabularInline): #테이블화시키기
	model = Choice
	extra = 2

class QuestionAdmin(admin.ModelAdmin):
	# fields = ['pub_date', 'question_text'] #필드순서 변경
	fieldsets = [ #그룹핑
		('Question Statement',{'fields':['question_text']}),
		('Date Information', {'fields':['pub_date']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date') # 레코드 리스트 항목 지정
	list_filter = ['pub_date'] #필터 사이드바 추가
	search_fields = ['question_text','pub_date'] #지정한 컬럼 에 대한 검색 박스 

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)


