from django import template as A
B=A.Library()
@B.inclusion_tag('downloads/templatetags/os_release_files.html')
def C(release,os_slug):'\n    Given a Relase object and os_slug return the files for that release\n    ';A=release;return{'release':A,'files':A.files_for_os(os_slug)}