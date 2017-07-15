
def per_display(tot_pages, now_page, number):
    # tot_pages 为页面总数  now_page 为当前页面  number为页面角标显示个数
    # 最终返回要显示的角标的列表
    if tot_pages <= number:
        page_list = range(1, tot_pages + 1)
    else:
        if now_page <= number-(number//2):
            page_list = range(1, number + 1)
        elif now_page <= tot_pages - (number//2):
            if number % 2 == 0:
                page_list = range(now_page - (number//2), now_page + (number//2))
            else:
                page_list = range(now_page - (number // 2), now_page + (number // 2)+1)
        else:
            page_list = range(tot_pages - (number-1), tot_pages + 1)
    return page_list