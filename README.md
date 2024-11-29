# midi_lang

# EBNF Grammar for MIDI Language

## Program Structure
```ebnf
script          ::= { statement };

statement       ::= tempo_statement
                  | key_statement
                  | timesig_statement
                  | track_statement
                  | note_statement
                  | rest_statement
                  | repeat_statement
                  | variable_assignment
                  | play_statement
                  | export_statement
                  | meta_statement
                  | dynamic_statement
                  | conditional_statement
                  | function_definition
                  | function_call
                  | while_statement;

tempo_statement ::= "tempo" number "bpm" ";";

key_statement   ::= "key" key_name key_type ";";

timesig_statement ::= "timesig" number "/" number ";";

track_statement ::= "track" number "on_channel" number ";";

note_statement  ::= note_name octave duration [ velocity ] [ "at" time ] ";";

rest_statement  ::= "rest" duration [ "at" time ] ";";

repeat_statement ::= "repeat" number "{" { statement } "}";

variable_assignment ::= "let" identifier "=" expression ";";

expression      ::= boolean_expression | numeric_expression;

numeric_expression ::= term { ("+" | "-" | "*" | "/") term };
term            ::= factor { ("*" | "/") factor };
factor          ::= number | identifier | "(" numeric_expression ")" ;

boolean_expression ::= boolean_term { ("&&" | "||") boolean_term };
boolean_term    ::= boolean_factor | "!" boolean_factor;
boolean_factor  ::= comparison | boolean_literal | identifier | "(" boolean_expression ")";
comparison      ::= numeric_expression ("<" | "<=" | ">" | ">=" | "==" | "!=") numeric_expression;

boolean_literal ::= "true" | "false";

conditional_statement ::= "if" "(" expression ")" "{" { statement } "}" [ "else" "{" { statement } "}" ];

while_statement ::= "while" "(" expression ")" "{" { statement } "}";

function_definition ::= "fn" identifier "(" [ parameter_list ] ")" "{" { statement } "}";

parameter_list  ::= identifier { "," identifier };

function_call   ::= identifier "(" [ argument_list ] ");";
argument_list   ::= expression { "," expression };

dynamic_statement ::= crescendo | decrescendo;

crescendo       ::= "crescendo" "{" { note_statement } "}" "from" velocity "to" velocity ";";

decrescendo     ::= "decrescendo" "{" { note_statement } "}" "from" velocity "to" velocity ";";

play_statement  ::= "play" identifier [ "at" time ] ";";

export_statement ::= "export" "\"" filename "\"" ";";

meta_statement ::= "metatext" "\"" text "\"" ";";

note_name       ::= "A" | "B" | "C" | "D" | "E" | "F" | "G" 
                  | "A#" | "C#" | "D#" | "F#" | "G#" 
                  | "Bb" | "Db" | "Eb" | "Gb" | "Ab";

chord_statement ::= "play chord" chord_name duration [ velocity ] ";";

chord_name      ::= note_name chord_type;
chord_type      ::= "maj" | "min" | "dim" | "aug" | "maj7" | "min7" | "7";

duration        ::= "whole" | "half" | "quarter" | "eighth" | "sixteenth";

velocity        ::= "piano" | "mezzo_piano" | "mezzo_forte" | "forte";

key_name        ::= note_name;
key_type        ::= "major" | "minor";

instrument_statement ::= "instrument" instrument_name ";";
instrument_name ::= "piano" | "strings" | "guitar" | "bass" | "drums" | ... ;

filename        ::= identifier;

time            ::= digit ":" digit;  (* Bars and beats *)
number          ::= digit { digit } [ "." digit { digit } ]; (* Integers and floats *)
identifier      ::= letter { letter | digit | "_" | "-" };
text            ::= { any_character };
digit           ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9";
letter          ::= "a" | "b" | "c" | ... | "z" | "A" | "B" | "C" | ... | "Z";
any_character   ::= ? any valid text character ? ;

```
