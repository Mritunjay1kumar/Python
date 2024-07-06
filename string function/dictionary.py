#dictionary {key:value}
#associative array
#define dictionary in { }
#donot save duplicate value
#update(),get(),pop(),items(),values(),keys(),clear()
x={"php":340,"vb":750,"java":500}
print(x)
x.update({'os':700,'jsp':300})
print(x)
print(x.get("java"))
x.pop('vb')
print(x)
print(x.items())
print(x.keys())
print(x.values())
x.clear()
print(x)

