from django.urls import path
from articles import views


urlpatterns = [
    path('', views.ArticleView.as_view(), name='article_list'),
    path('<int:article_id>', views.ArticleDetailView.as_view(), name='article_detail'),
    path('test', views.KakaoMapView.as_view(), name='test_map'),
    path('<int:article_id>/comments/', views.CommentView.as_view(), name='comment_view'), # 댓글 생성 / 조회 / 수정 / 삭제
]