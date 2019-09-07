from django.conf import settings
from ..user.models import *
from utils.Mixin import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse
from django.views import View
import re
from django.db.models import Q
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

def index(request):
    items = Item.objects.filter(is_found=0)
    types = Type.objects.all()
    found_number = len(Item.objects.filter(is_found=1))
    lost_number = len(Item.objects.filter(is_found=0))
    return render(request, 'index.html', {'item_types':types,'found_number':found_number,'lost_number':lost_number,'items':items})


class release_view(LoginRequiredMixin,View):
    def get(self, request):
        item_types = Type.objects.all()
        return render(request, 'the_release.html', {'item_types': item_types})

        # return render(request, 'login.html')

    def post(self, request):
        item_email = request.POST.get('item_email')
        item_telephone = request.POST.get('item_telephone')
        status = request.POST.get('status')
        area = request.POST.get('area')
        item_type = request.POST.get('item_type')
        item_type = Type.objects.get(name=item_type)


        print(item_type)
        time = request.POST.get('time')
        location = request.POST.get('location')
        price = request.POST.get('price')
        detail = request.POST.get('detail')
        user_id = request.POST.get('user_id')
        item_user = User.objects.get(id=user_id)
        item_id = request.POST.get('item_id')


        if item_id:
            item = Item.objects.get(id=item_id)
            item.item_email = request.POST.get('item_email')
            item.item_telephone = request.POST.get('item_telephone')
            item.status = request.POST.get('status')
            item.area = request.POST.get('area')
            item.time = request.POST.get('time')
            item.location = request.POST.get('location')
            item.price = request.POST.get('price')
            item.detail = request.POST.get('detail')
            i = 0
            pics = request.FILES.getlist('pic')

            for pic in pics:
                save_path = '%s/%s' % (settings.MEDIA_ROOT, pic.name)
                with open(save_path, 'wb+') as f:
                    for content in pic.chunks():
                        f.write(content)
                    f.close()
                    print(pic.name)
                    item = Item.objects.get(id=item_id)
                    if i == 0:
                        item.picture.pic1 = pic.name
                    elif i == 1:
                        item.picture.pic2 = pic.name
                    else:
                        item.picture.pic3 = pic.name
                    i += 1
            item.picture.item = item
            item.picture.save()

            item.item_type = item_type
            item.item_user = item_user
            item.save()
        else:
            picture = Picture()
            item = Item(item_email=item_email, item_telephone=item_telephone, status=status, time=time, area=area,
                    location=location, detail=detail, price=price)
            item.item_type = item_type
            item.item_user = item_user
            item.save()
            i = 0
            pics = request.FILES.getlist('pic')

            for pic in pics:
                save_path = '%s/%s' % (settings.MEDIA_ROOT, pic.name)
                with open(save_path, 'wb+') as f:
                    for content in pic.chunks():
                        f.write(content)
                    f.close()
                    print(pic.name)
                    if i == 0:
                        picture.pic1 = pic.name
                    elif i == 1:
                        picture.pic2 = pic.name
                    else:
                        picture.pic3 = pic.name
                    i += 1
            picture.item = item
            picture.save()
        return redirect(reverse('ITEM:index'))
def release_edit(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item = Item.objects.get(pk=item_id)
        item.item_email = request.POST.get('item_email')
        item.item_telephone = request.POST.get('item_telephone')
        item.status = request.POST.get('status')
        item.area = request.POST.get('area')
        print(item.area)
        item_type = request.POST.get('item_type')
        print(item.item_type.name)
        item.time = request.POST.get('time')
        item.location = request.POST.get('location')
        item.price = request.POST.get('price')
        item.detail = request.POST.get('detail')
        item_type = Type.objects.get(name=item_type)
        item_user = User.objects.first()
        item.item_type = item_type
        item.item_user = item_user
        print(item.item_type)
        item.save()
        pics = request.FILES.getlist('pic')
        print(pics)
        i = 0
        for pic in pics:
            save_path = '%s/%s' % (settings.MEDIA_ROOT, pic.name)
            with open(save_path, 'wb+') as f:
                for content in pic.chunks():
                    f.write(content)
                f.close()
                print(pic.name)
                if i == 0:
                    item.picture.pic1 = pic.name
                elif i == 1:
                    item.picture.pic2 = pic.name
                else:
                    item.picture.pic3 = pic.name
                i += 1
        item.picture.item = item
        item.picture.save()
        item.save()
        return redirect(reverse('myRelease'))
    else:
        raise RuntimeError("修改信息的method错误")

class detail_view(View):
    def get(self, request, item_id):
        try:
            item = Item.objects.get(id=item_id)
            time = item.create_time
            create_time = str(time)[0:10]
            user = User.objects.get(id=item.item_user_id)
            qq = item.item_email[:-6]

        except Item.DoesNotExist:
            return redirect(reverse('ITEM:index'))
        return render(request, 'detail.html', {'item':item, 'qq':qq,'release_user':user,'create_time':create_time})

def fuzzyfinder(user_input, collection):  # 模糊查找
    suggestions = []
    pattern = '.*?'.join(user_input)  # Converts 'djm' to 'd.*?j.*?m'
    regex = re.compile(pattern)  # Compiles a regex.
    for item in collection:
        match = regex.search(item)  # Checks if the current item matches the regex.
        if match:
            suggestions.append((len(match.group()), match.start(), item))
    return [x for _, _, x in sorted(suggestions)]


def search(request):
    types = Type.objects.all()
    found_number = len(Item.objects.filter(is_found=1))
    lost_number = len(Item.objects.filter(is_found=0))
    if request.method == 'POST':
        items = Item.objects.all()
        q = request.POST.get('q')
        print(q)
        details = []
        locations = []
        item_details = []
        for item in items:
            details.append(item.detail)
            locations.append(item.location)
        result = fuzzyfinder(q, details)
        if result:
            for i in range(len(result)):
                item_detail = Item.objects.filter(detail=result[i])
                if len(item_detail)>1:
                    item_details.append(item_detail[i])
                else:
                    item_details.append(item_detail[0])
            return render(request, 'search.html', {'items': item_details, 'item_types': types,'found_number':found_number,'lost_number':lost_number})
        else:
            result = fuzzyfinder(q, locations)
            for i in range(len(result)):
                item_detail = Item.objects.filter(location=result[i])
                if len(item_detail)>1:
                    item_details.append(item_detail[i])
                else:
                    item_details.append(item_detail[0])
            return render(request, 'search.html', {'items': item_details, 'item_types': types,'found_number':found_number,'lost_number':lost_number})
    else:
        return render(request, 'index.html', {'item_types': types,'found_number':found_number,'lost_number':lost_number})


def item_edit(request, item_id):
    item = Item.objects.get(id=item_id)
    item_types = Type.objects.all()
    return render(request, 'the_release.html', {'item_types': item_types, 'item':item})

def lost(request):
    types = Type.objects.all()
    items = Item.objects.filter(status='失物')
    found_number = len(Item.objects.filter(is_found=1))
    lost_number = len(Item.objects.filter(is_found=0))
    return render(request, 'found.html', {'items':items,'found_number':found_number,'lost_number':lost_number,'item_types':types})

def found(request):
    types = Type.objects.all()
    items = Item.objects.filter(status='拾物')
    found_number = len(Item.objects.filter(is_found=1))
    lost_number = len(Item.objects.filter(is_found=0))
    return render(request, 'found.html', {'items':items,'found_number':found_number,'lost_number':lost_number,'item_types':types})

def all_found(request):
    types = Type.objects.all()
    items = Item.objects.filter(is_found=1)
    found_number = len(items)
    lost_number = len(Item.objects.filter(is_found=0))
    return render(request,'all_found.html',{'items':items,'found_number':found_number,'lost_number':lost_number,'item_types':types})

def index_search(request):
    types = Type.objects.all()
    found_number = len(Item.objects.filter(is_found=1))
    lost_number = len(Item.objects.filter(is_found=0))
    if request.method == 'POST':
        try:
            item_type = request.POST.get('item_type')
            item_type = Type.objects.get(name=item_type)
            status = request.POST.get('status')
            area = request.POST.get('area')
            items = Item.objects.filter(Q(item_type=item_type)&Q(status=status)&Q(area=area))
            return render(request,'search.html',{'items':items,'found_number':found_number,'lost_number':lost_number,'item_types':types})
        except:
            return redirect(reverse('ITEM:index'))
    else:
        return render(request,'index.html',{'item_types':types,'found_number':found_number,'lost_number':lost_number})


