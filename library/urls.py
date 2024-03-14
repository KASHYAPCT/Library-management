from django.urls import path
from library import views
urlpatterns = [
    path('',views.index,name="indexpage"),
    path('login/',views.logboth,name="loginpage"),
    path('reg/',views.regform,name="regform"),
    path('admnlog/',views.admnlog,name="adminlog"),
    path('studlog/',views.studlog,name="studlog"),
    path('add_book/',views.addbook,name='addbook'),
    path('view_book/',views.view_admbook,name="viewbook"),
    path('update_book/',views.update_book,name="updatebook"),
    path('view_studbook/',views.view_studbook,name='sudentbookview'),
    path('logout/',views.both_logout,name="logout"),
    path('bsearch/',views.book_search,name="booksearchupdate"),
    path('edit/<Book_id>',views.book_edit,name="bookedit"),
    path('delete/<int:id>',views.deletebook,name="bookdelete"),
    path("orderbook/",views.order_book,name="orderbook"),
    path("orderdetials/",views.order_bookdetials,name="oderbookdetials"),
    path("admorderview/",views.adm_view_order,name="adminvieworder"),
    path('oderconfirm/<int:id>/<book_id>',views.adm_confirmation,name="adminconfirmation"),
    path('viewdateinfo/',views.view_dateinfo,name="stud_date_info"),
    path('return_book/<int:id>/<book_id>',views.stud_return_book,name="stud_return_book"),
]