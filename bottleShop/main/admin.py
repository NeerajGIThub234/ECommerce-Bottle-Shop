from django.contrib import admin
from .models import Category,Brand,Color,Size,Product,ProductAttribute,Banner,CartOrder,CartOrderItems,ProductReview,WishList,UserAddressBook

admin.site.register(Size)

class BannerAdmin(admin.ModelAdmin):
    list_display=('alt_text','image_tage') #to show image
admin.site.register(Banner,BannerAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display=('title','image_tage') #to show image
admin.site.register(Category,CategoryAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display=('title','image_tage')
admin.site.register(Brand,BrandAdmin)

class ColorAdmin(admin.ModelAdmin):
    list_display=('title','color_bg')
admin.site.register(Color,ColorAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','title','category','brand','status','is_featured')# to show all this paramet on product
    list_editable=('status','is_featured') # to edit the status
admin.site.register(Product,ProductAdmin)

# Product Attributes
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display=('id','image_tage','product','price','color','size')
admin.site.register(ProductAttribute,ProductAttributeAdmin)     

#Order
class CartOrderAdmin(admin.ModelAdmin):
    list_editable=('paid_status','order_status') # bcz this it show checkbox 
    list_display=('user','total_amt','paid_status','order_dt','order_status') 
admin.site.register(CartOrder,CartOrderAdmin)

#Order Items
class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display=('invoice_no','item','image_tage','qty','price','total') 
admin.site.register(CartOrderItems,CartOrderItemsAdmin)

#Order Items
class ProductReviewAdmin(admin.ModelAdmin):
    list_display=('user','product','review_text','get_review_rating') 
admin.site.register(ProductReview,ProductReviewAdmin)

#WishList 
admin.site.register(WishList)


#User Address Book
class UserAddressBookAdmin(admin.ModelAdmin):
    list_display=('user','address','status') 
admin.site.register(UserAddressBook,UserAddressBookAdmin)