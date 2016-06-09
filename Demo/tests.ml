
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

close_out oc;
					exit 0;;
					