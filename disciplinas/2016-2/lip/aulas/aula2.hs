zeroto n = [0..n]
add (x,y) = x+y

add' :: Int -> (Int -> Int)
add' x y = x + y


add'' = add' 3

myfunction = take 2

twice f x = f (f x)
