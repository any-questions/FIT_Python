# TODO Найдите количество книг, которое можно разместить на дискете
v_disk=1.44
num_pages=100
num_str_on_pg=50
num_symbls_in_str=25
v_one_symbl=4
v_disk_byte=1.44*1024*1024
v_one_book=100*50*25*4
num_of_books=v_disk_byte//v_one_book
print("Количество книг, помещающихся на дискету:", int(num_of_books))
