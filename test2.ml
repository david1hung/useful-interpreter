
open Printf

let testNum = ref (1);;
let file = "testOutput2.txt";;
let oc = open_out file;;

let printToFile msg = 
	fprintf oc "Test %d: %s\n" !testNum msg;
	testNum := (!testNum+1);
;;


let rec rev n =
	match n with
    [] -> []
    | first::rest -> rev(rest)@[first]
;;
if (rev [1;2;3;4;5] =  [5; 4; 3; 2; 1] ) then printToFile "Success" else printToFile "Failed";;
if (rev [5;4;3;2;1] =  [1; 2; 3; 4; 5] ) then printToFile "Success" else printToFile "Failed";; let rec intOfDigits (l: int list) : int =
	match l with
    []->0
    |[last]->last
    |cur::next::rest -> intOfDigits(cur*10+next::rest)
;;
if (intOfDigits([1;2;3;4;5]) =  12345 ) then printToFile "Success" else printToFile "Failed";;

close_out oc;