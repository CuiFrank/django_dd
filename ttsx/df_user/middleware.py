from django.shortcuts import render,redirect


class UrlPathMiddleWare():

    #处理视图前中间件函数，会将静态文件路径去除，剩下真正能匹配视图的url，所以选择这个中间件
    def process_view(self, request, view_func, view_args, view_kwargs):

    # 在开发阶段，没有部署nginx时，当请求的网页中的静态文件没找到时，url后面就会加上静态文件的路径，
    # 导致在下面的函数中进行列表中元素判断时，无法排除，如果真实运行后，部署了nginx，静态文件加载就不会走uwsig这条路
    # 处理请求前的中间件函数
    # def process_request(request):

        # 这是获得全路径的一个方法 /user/register_name/?name=frank 后面携带参数
        # path = request.get_full_path()
        # 这是获得路径的一个属性 /user/register_name/ 后面不携带参数
        path = request.path
        # print(path + 'hsssss')
        if path not in ['/user/login/', '/center/is_login/', '/user/register/',
                    '/user/register_handle/', '/user/login_handle/',
                    '/user/register_name/','/',  ]:
            request.session['url_path'] = path
            # print(path+'haha')
        # else:
        #     request.session['url_path'] = '/user/login/'


