
open Printf

#use "code.ml" ;;

let testNum = ref (1);;
let file = "testOutput.txt";;
let oc = open_out file;;

let printToFile msg = 
	fprintf oc "Test %d: %s\n" !testNum msg;
	testNum := (!testNum+1);
;;




close_out oc;
					exit 0;;
					