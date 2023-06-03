echo Enter scene filename: 
read scenename + '.py'
echo Class name: 
read classname
manim -pqh $scenename $classname
