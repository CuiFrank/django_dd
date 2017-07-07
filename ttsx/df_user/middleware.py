from django.shortcuts import render,redirect


class UrlPathMiddleWare():
    def process_request(self,request):
        path = request.get_full_path()
        if path not in ['/user/login/', '/user/register/',
                    '/user/register_handle/', '/user/login_handle/',
                    '/user/register_name/', ]:
            request.session['url_path'] = path
            # print(path+'haha')
        # else:
        #     request.session['url_path'] = '/user/login/'


