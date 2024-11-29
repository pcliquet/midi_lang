# Propositional Language

# EBNF Grammar for Propositional Language

## Program Structure
```ebnf
program                       ::= { function_declaration } ;

function_declaration          ::= "fn" , identifier , "(" , [ parameter_list ] , ")" , ":" , type , block ;

parameter_list                ::= parameter , { "," , parameter } ;
parameter                     ::= identifier , ":" , type ;

block                         ::= "{" , { statement , ";" } , "}" ;

statement                     ::= 
                                   λ
                                 | print_statement
                                 | declaration_statement
                                 | assignment_statement
                                 | func_call_statement
                                 | while_statement
                                 | for_statement
                                 | if_statement
                                 | function_declaration ;

print_statement               ::= "print" , "(" , string , [ "," , expression , { "," , expression } ] , ")" ;

declaration_statement         ::= identifier_decl , ":" , type , ";" ;

identifier_decl               ::= identifier , [ "=" , expression ] , { "," , identifier , [ "=" , expression ] } ;



assignment_statement          ::= identifier , "=" , expression ;

if_statement                  ::= "if" , "(" , expression , ")" , block , [ "else" , block ] ;

while_statement               ::= "while" , "(" , expression , ")" , block ;

for_statement                 ::= "for" , "(" , assignment_statement , ";" , expression , ";" , assignment_statement , ")" , block ;

func_call_statement           ::= identifier , "(" , [ argument_list ] , ")" ;

argument_list                 ::= expression , { "," , expression } ;

expression                    ::= biconditional , { ( "==" | "<" | ">" ) , biconditional } ;

biconditional                 ::= implication , { ( "↔" | "<->" ) , implication } ;

implication                   ::= disjunction , { ( "→" | "->" ) , disjunction } ;

disjunction                   ::= conjunction , { ( "∨" | "||" ) , conjunction } ;

conjunction                   ::= sum , { ( "∧" | "&&" ) , sum } ;

sum                           ::= term , { ( "+" | "-" ) , term } ;

term                          ::= factor , { ( "*" | "/" ) , factor } ;

factor                        ::= [ "+" | "-" | ( "¬" | "!" | "~" ) ] , atom ;

atom                          ::= "(" , expression , ")" | identifier | number | log;

number                        ::= digit , { digit } ;

log                           ::= "verum" | "falsum" ;

type                          ::= "int" |  "log" | "empty";

string                        ::= '"' , { character } , '"' ;

identifier                    ::= letter , { letter | digit | "_" } ;

letter                        ::= "a" | "b" | ... | "z" | "A" | "B" | ... | "Z" ;

digit                         ::= "0" | "1" | ... | "9" ;

character                     ::= letter | digit | " " | any_other_printable_character ;

```
