let rec rev n = 
	match n with 
    [] -> []
    | first::rest -> rev(rest)@[first] ;;




(* let rec intOfDigits (l: int list) : int =
	match l with
    []->0 
    |[last]->last
    |cur::next::rest -> intOfDigits(cur*10+next::rest) ;; *) 
 