# midi_lang

# EBNF Grammar for MIDI Language

## Program Structure
```ebnf
<PROGRAM> ::= <STATEMENT>* ;

<STATEMENT> ::= <VARIABLE_DECLARATION> 
              | <VARIABLE_ASSIGNMENT>
              | <TEMPO_STATEMENT> 
              | <NOTE_STATEMENT>
              | <LOOP_STATEMENT>
              | <IF_STATEMENT> ;

<LOOP_STATEMENT> ::= "loop" "(" <RELATIONAL_EXPRESSION> ")" <BLOCK> ;

<IF_STATEMENT> ::= "if" "(" <RELATIONAL_EXPRESSION> ")" <BLOCK> [ "else" <BLOCK> ] ;

<BLOCK> ::= "{" <STATEMENT>* "}" ;

<TEMPO_STATEMENT> ::= "tempo" "=" <EXPRESSION> ";" ;

<PLAY_STATEMENT> ::= "play" <RELATIONAL_EXPRESSION> <RELATIONAL_EXPRESSION> 
[<RELATIONAL_EXPRESSION>] [ "at" <RELATIONAL_EXPRESSION>] ";" ;

<VARIABLE_DECLARATION> ::= <TYPE> <IDENTIFIER> ["[" <RELATIONAL_EXPRESSION> "]"]
[ "=" <RELATIONAL_EXPRESSION> ] ( "," <IDENTIFIER> [ "=" <RELATIONAL_EXPRESSION> ] )* ";" ;

<VARIABLE_ASSIGNMENT> ::= <IDENTIFIER> ["[" <RELATIONAL_EXPRESSION> "]"]
"=" <RELATIONAL_EXPRESSION> ";" ;

<EXPRESSION> ::= <TERM> ( ("||" | "+" | "-") <TERM> )* ;

<RELATIONAL_EXPRESSION> ::= <EXPRESSION> ( ("==" | "!=" | "<" | ">" | "<=" | ">=")
<EXPRESSION> )? ;


<TERM> ::= <FACTOR> ( ("*" | "/" | "&&") <FACTOR> )* ;


<FACTOR> ::= ( ("+" | "-" | "!") <FACTOR> )
           | <NUMBER>
           | "(" <RELATIONAL_EXPRESSION> ")"
           | <IDENTIFIER>
           | <NOTE>
           | <CHORD> ;



<CHORD> ::= "[" <NOTE> ( "," <NOTE> )* "]" ;

<NOTE> ::= <NOTE_NAME> <OCTAVE> ;

<NOTE_NAME> ::= "A" | "B" | "C" | "D" | "E" | "F" | "G" [ "#" | "b" ] ;

<OCTAVE> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" ;

<DURATION> ::= <NUMBER> ;

<IDENTIFIER> ::= <LETTER> (<LETTER> | <DIGIT> | "_")* ;

<LETTER> ::= "a" | ... | "z" | "A" | ... | "Z" ;

<NUMBER> ::= <DIGIT>+ ;

<DIGIT> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

<TYPE> ::= "INT" | "NOTE" | "CHORD";
```
