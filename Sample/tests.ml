
open Printf

#use "code.ml" ;;

let testNum = ref (1);;
let file = "testOutput.txt";;
let oc = open_out file;;

let printToFile msg = 
	fprintf oc "Test %d: %s\n" !testNum msg;
	testNum := (!testNum+1);
;;



if (rev [1;2;3] =  [3; 2; 1] ) then printToFile "Success" else printToFile "Failed";;
if (rev [1;2;3] =  [3; 2] ) then printToFile "Success" else printToFile "Failed";;let rec intOfDigits (l: int list) : int =
	match l with
    []->0
    |[last]->last
    |cur::next::rest -> intOfDigits(cur*10+next::rest) 
;;
if (intOfDigits [1;2;3;4;5] =  12345 ) then printToFile "Success" else printToFile "Failed";;

close_out oc;
					exit 0;;
					