# import module_4_1_1
# # print(dir(module_4_1_1))
# print('Привет я из модуля 1')
# print(module_4_1_1.a)
# module_4_1_1.say_hi()


# import module_4_1_1 as m4
# # print(dir(module_4_1_1))
# print('Привет я из модуля 1')
# print(m4.a)
# m4.say_hi()


# from module_4_1_1 import a, b, say_hi #from  для вызова глобальных переменных
# # print(dir(module_4_1_1))
# print('Привет я из модуля 1')
# say_hi()
# print(a)
# print(b)


# from module_4_1_1 import * #импорт всех переменных и ф-й,
# #отдельная ф-я print срабатывает в любом случае(первой)
# # print(dir(module_4_1_1))
# print('Привет я из модуля 1')
# say_hi()
# print(a)
# print(b)


# import module_4_1_1 as m4
# # print(dir(module_4_1_1))
# print('Привет я из модуля 1')
# print(m4.__name__)
# print(m4.main())



# from module_4_1_1 import say_hi as sh
# print('Привет я из модуля 1')
# sh()



from fake_math import divide as fm_d
from true_math import divide as tm_d
result1 = fm_d(69, 3)
result2 = fm_d(3, 0)
result3 = tm_d(49, 7)
result4 = tm_d(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)
























