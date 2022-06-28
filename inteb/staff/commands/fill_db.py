from staff.models import IntebUser
from django.core.management.base import BaseCommand
import json, os

from tasks.models import IntebTasks, TaskComment, TaskPictures

JSON_PATH = 'staff/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), mode='r', encoding='UTF-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        tasks = load_from_json('tasks')

        IntebTasks.objects.all().delete()
        for task in tasks:
            new_task = IntebTasks(**task)
            new_task.save()

        products = load_from_json('products')
        taskcomments = load_from_json('taskcomments')
        TaskComment.objects.all().delete()
        for comment in taskcomments:
            task_id = comment['task']
            _task =
        Product.objects.all().delete()
        for product in products:
            category_id = product['category']
            _category = ProductCategory.objects.get(pk=category_id)

            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

        ShopUser.objects.create_superuser('admin', "admin@geekshop.local", '548365', age=35)