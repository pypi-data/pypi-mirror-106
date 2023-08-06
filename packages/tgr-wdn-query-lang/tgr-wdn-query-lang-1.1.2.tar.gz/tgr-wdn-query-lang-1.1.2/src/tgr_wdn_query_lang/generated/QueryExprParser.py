# Generated from QueryExprParser.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("#\4\2\t\2\4\3\t\3\3\2\7\2\b\n\2\f\2\16\2\13\13\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\5\3\36\n\3\3\3\5\3!\n\3\3\3\2\2\4\2\4\2\2\2&")
        buf.write("\2\t\3\2\2\2\4\35\3\2\2\2\6\b\5\4\3\2\7\6\3\2\2\2\b\13")
        buf.write("\3\2\2\2\t\7\3\2\2\2\t\n\3\2\2\2\n\f\3\2\2\2\13\t\3\2")
        buf.write("\2\2\f\r\7\2\2\3\r\3\3\2\2\2\16\17\7\3\2\2\17\20\7\5\2")
        buf.write("\2\20\36\7\21\2\2\21\22\7\3\2\2\22\23\7\5\2\2\23\36\7")
        buf.write("\22\2\2\24\25\7\3\2\2\25\26\7\5\2\2\26\36\7\16\2\2\27")
        buf.write("\30\7\3\2\2\30\31\7\5\2\2\31\36\7\17\2\2\32\33\7\3\2\2")
        buf.write("\33\34\7\5\2\2\34\36\7\20\2\2\35\16\3\2\2\2\35\21\3\2")
        buf.write("\2\2\35\24\3\2\2\2\35\27\3\2\2\2\35\32\3\2\2\2\36 \3\2")
        buf.write("\2\2\37!\7\f\2\2 \37\3\2\2\2 !\3\2\2\2!\5\3\2\2\2\5\t")
        buf.write("\35 ")
        return buf.getvalue()


class QueryExprParser ( Parser ):

    grammarFileName = "QueryExprParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'!='", "'>'", "'>='", "'<'", "'<='", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'NULL'" ]

    symbolicNames = [ "<INVALID>", "IDENTIFIER", "WS", "OPERATOR", "EQ", 
                      "NE", "GT", "GE", "LT", "LE", "LABEL", "DELIMITER", 
                      "NUMBER", "BOOL", "NULL", "STRING", "STRING_QUOTED" ]

    RULE_exprs = 0
    RULE_expr = 1

    ruleNames =  [ "exprs", "expr" ]

    EOF = Token.EOF
    IDENTIFIER=1
    WS=2
    OPERATOR=3
    EQ=4
    NE=5
    GT=6
    GE=7
    LT=8
    LE=9
    LABEL=10
    DELIMITER=11
    NUMBER=12
    BOOL=13
    NULL=14
    STRING=15
    STRING_QUOTED=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(QueryExprParser.EOF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QueryExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(QueryExprParser.ExprContext,i)


        def getRuleIndex(self):
            return QueryExprParser.RULE_exprs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprs" ):
                listener.enterExprs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprs" ):
                listener.exitExprs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprs" ):
                return visitor.visitExprs(self)
            else:
                return visitor.visitChildren(self)




    def exprs(self):

        localctx = QueryExprParser.ExprsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_exprs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==QueryExprParser.IDENTIFIER:
                self.state = 4
                self.expr()
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 10
            self.match(QueryExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(QueryExprParser.IDENTIFIER, 0)

        def OPERATOR(self):
            return self.getToken(QueryExprParser.OPERATOR, 0)

        def STRING(self):
            return self.getToken(QueryExprParser.STRING, 0)

        def STRING_QUOTED(self):
            return self.getToken(QueryExprParser.STRING_QUOTED, 0)

        def NUMBER(self):
            return self.getToken(QueryExprParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(QueryExprParser.BOOL, 0)

        def NULL(self):
            return self.getToken(QueryExprParser.NULL, 0)

        def LABEL(self):
            return self.getToken(QueryExprParser.LABEL, 0)

        def getRuleIndex(self):
            return QueryExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = QueryExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 12
                self.match(QueryExprParser.IDENTIFIER)
                self.state = 13
                self.match(QueryExprParser.OPERATOR)
                self.state = 14
                self.match(QueryExprParser.STRING)
                pass

            elif la_ == 2:
                self.state = 15
                self.match(QueryExprParser.IDENTIFIER)
                self.state = 16
                self.match(QueryExprParser.OPERATOR)
                self.state = 17
                self.match(QueryExprParser.STRING_QUOTED)
                pass

            elif la_ == 3:
                self.state = 18
                self.match(QueryExprParser.IDENTIFIER)
                self.state = 19
                self.match(QueryExprParser.OPERATOR)
                self.state = 20
                self.match(QueryExprParser.NUMBER)
                pass

            elif la_ == 4:
                self.state = 21
                self.match(QueryExprParser.IDENTIFIER)
                self.state = 22
                self.match(QueryExprParser.OPERATOR)
                self.state = 23
                self.match(QueryExprParser.BOOL)
                pass

            elif la_ == 5:
                self.state = 24
                self.match(QueryExprParser.IDENTIFIER)
                self.state = 25
                self.match(QueryExprParser.OPERATOR)
                self.state = 26
                self.match(QueryExprParser.NULL)
                pass


            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QueryExprParser.LABEL:
                self.state = 29
                self.match(QueryExprParser.LABEL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





