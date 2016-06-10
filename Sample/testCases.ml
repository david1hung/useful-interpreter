# rev [1;2;3];;
- : int list = [3; 2; 1]

# rev [1;2;3];;
- : int list = [3; 2]

# let rec intOfDigits (l: int list) : int =
	match l with
    []->0 
    |[last]->last
    |cur::next::rest -> intOfDigits(cur*10+next::rest) ;;         
val intOfDigits : int list -> int = <fun>
# intOfDigits [1;2;3;4;5];;
- : int = 12345