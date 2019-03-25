from django.db import models
from datetime import datetime

class UserReport(models.Model):
    """
    个人用户获取报告表 生产环境
    """
    # 报告编号
    id = models.AutoField(primary_key=True)
    # 报告状态 0:生成中； 1：成功； 2：失败
    status = models.CharField(max_length=50, default=0, db_index=True)
    # 报告完成返回的地址url
    url = models.CharField(max_length=256, null=True, blank=True, default="", db_index=True)
    # 添加时间
    add_time = models.DateTimeField(auto_now_add=True)
    # 关联报告模型
    report_type_id = models.CharField(max_length=50, default=0, db_index=True)

    people_result_id = models.BigIntegerField(default=0, db_index=True)

    try_times = models.PositiveIntegerField(default=0, db_index=True)
    # Django数据模型的内部数据限制类
    class Meta:
        # 控制数据查询时的排序方式
        ordering = ["-id"]