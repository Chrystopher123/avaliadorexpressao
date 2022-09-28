import sys
import parser_compiler
import lexer_compiler
import derivation_tree_generator
import symbol_table_compiler

if __name__ == "__main__":
    stream = None
    try:
        file_path = sys.argv[1]
        file = open(file_path, 'r')
        stream = file.read()
    except:
        stream = "numero = 9\n"
        stream += "\nresultado = (9 + 20) - 3 * (5 ** 3) / 55 + sin(numero)\n"
        stream += "resultado + 90"

    lexer = lexer_compiler.Lexer(stream)
    tokens = lexer.create_tokens()
    derivation_tree_generator_instace = derivation_tree_generator.DerivationTreeGenerator(tokens)
    derivation_tree = derivation_tree_generator_instace.create_tree()
    symbol_table_instance = symbol_table_compiler.SymbolTable()
    parser = parser_compiler.Parser(symbol_table_instance)
    result = parser.parse(derivation_tree)
    print(result)