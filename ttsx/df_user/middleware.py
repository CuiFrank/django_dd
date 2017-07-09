from django.shortcuts import render,redirect


class UrlPathMiddleWare():
    def process_view(self,request, view_func, view_args, view_kwargs):
        path = request.get_full_path()
        # print(path + 'hsssss')
        if path not in ['/user/login/', '/user/register/',
                    '/user/register_handle/', '/user/login_handle/',
                    '/user/register_name/','/',  ]:
            request.session['url_path'] = path
            # print(path+'haha')
        # else:
        #     request.session['url_path'] = '/user/login/'


