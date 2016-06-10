let rec rev n = 
	match n with 
    [] -> []
    | first::rest -> rev(rest)@[first] ;;
