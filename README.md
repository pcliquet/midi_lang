# midi_lang

# EBNF Grammar for MIDI Language

## Program Structure
```ebnf
would this work then?
program 		      ::= { statement} ;


block                         ::= "{" , { statement , ";" } , "}" ;

statement                     ::= 
                                  {
                                  print_statement
                                 | declaration_statement
                                 | assignment_statement
                                 | while_statement
                                 | for_statement
                                 | if_statement };

print_statement               ::= "exhibit" , "(" , string , [ "," , expression , { "," , expression } ] , ")", ";";

declaration_statement         ::= identifier_decl , ":" , type , ";" ;

identifier_decl               ::= identifier , [ "=" , expression ] , { "," , identifier , [ "=" , expression ] }, ";" ;



assignment_statement          ::= identifier , "=" , expression ;

if_statement                  ::= "branch" , "(" , expression , ")" , block , [ "else" , block ] ;

while_statement               ::= "while" , "(" , expression , ")" , block ;

for_statement                 ::= "for" , "(" , assignment_statement , ";" , expression , ";" , assignment_statement , ")" , block ;

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

type                          ::= "int" |  "log";

string                        ::= '"' , { character } , '"' ;

identifier                    ::= letter , { letter | digit | "_" } ;

letter                        ::= "a" | "b" | ... | "z" | "A" | "B" | ... | "Z" ;

digit                         ::= "0" | "1" | ... | "9" ;

character                     ::= letter | digit | " " | any_other_printable_character ;

```

