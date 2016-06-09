open Printf

#use "code.ml";;

let testNum = ref (1);;
let file = "testOutput.txt";;
let oc = open_out file;;

let printToFile msg = 
	fprintf oc "Test %d: %s\n" !testNum msg;
	testNum := (!testNum+1);
;;


if (rev [1;2;3;4;5] = [5;4;3;2;1]) then printToFile "Success" else printToFile "Failed";;
if (rev [5;4;3;2;1] = [1;2;3;4;5]) then printToFile "Success" else printToFile "Failed";;


close_out oc;
