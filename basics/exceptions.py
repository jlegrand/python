num = 1

try:
    print(num/den)
# except NameError:
#     print('variable non definie')
# except (TypeError, ZeroDivisionError):
#     print('erreur type ou zero')
except Exception as e:
    print('type : ', type(e).__name__)
    print('message : ', e)
    print(repr(e))
else:
    print('else')
finally:
    print('finally')


###
var = 5

assert var == 8