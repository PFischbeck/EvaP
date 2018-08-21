from django.template import Library
from evap.evaluation.models import Semester

register = Library()


@register.inclusion_tag("navbar.html")
def include_navbar(user, language, in_staff_mode):
    return {
        'user': user,
        'language': language,
        'in_staff_mode': in_staff_mode,
        'published_result_semesters': Semester.get_all_with_published_unarchived_results(),
        'result_semesters': Semester.get_all_with_unarchived_results(),
        'grade_document_semesters': Semester.objects.filter(grade_documents_are_deleted=False),
    }
