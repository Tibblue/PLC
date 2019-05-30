# Generated from gramatica.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("\67\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\6")
        buf.write("\2\17\n\2\r\2\16\2\20\3\2\3\2\7\2\25\n\2\f\2\16\2\30\13")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\6\3\37\n\3\r\3\16\3 \3\4\3\4\3")
        buf.write("\4\3\4\3\4\5\4(\n\4\3\4\3\4\3\4\3\5\3\5\6\5/\n\5\r\5\16")
        buf.write("\5\60\3\6\3\6\3\6\3\6\3\6\2\2\7\2\4\6\b\n\2\2\2\66\2\f")
        buf.write("\3\2\2\2\4\36\3\2\2\2\6\"\3\2\2\2\b,\3\2\2\2\n\62\3\2")
        buf.write("\2\2\f\16\5\4\3\2\r\17\7\r\2\2\16\r\3\2\2\2\17\20\3\2")
        buf.write("\2\2\20\16\3\2\2\2\20\21\3\2\2\2\21\22\3\2\2\2\22\26\5")
        buf.write("\b\5\2\23\25\7\r\2\2\24\23\3\2\2\2\25\30\3\2\2\2\26\24")
        buf.write("\3\2\2\2\26\27\3\2\2\2\27\31\3\2\2\2\30\26\3\2\2\2\31")
        buf.write("\32\7\2\2\3\32\3\3\2\2\2\33\34\5\6\4\2\34\35\7\r\2\2\35")
        buf.write("\37\3\2\2\2\36\33\3\2\2\2\37 \3\2\2\2 \36\3\2\2\2 !\3")
        buf.write("\2\2\2!\5\3\2\2\2\"#\7\13\2\2#$\7\3\2\2$\'\7\b\2\2%&\7")
        buf.write("\4\2\2&(\5\n\6\2\'%\3\2\2\2\'(\3\2\2\2()\3\2\2\2)*\7\5")
        buf.write("\2\2*+\5\n\6\2+\7\3\2\2\2,.\7\6\2\2-/\7\n\2\2.-\3\2\2")
        buf.write("\2/\60\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61\t\3\2\2\2")
        buf.write("\62\63\7\f\2\2\63\64\7\7\2\2\64\65\7\t\2\2\65\13\3\2\2")
        buf.write("\2\7\20\26 \'\60")
        return buf.getvalue()


class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'CREATE'", "'WITH'", "'FROM'", "'STATES'", 
                     "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "BOT_TYPE", "FILE_TYPE", 
                      "STATE", "PRIORIDADE", "STRING", "NEWLINE", "WS" ]

    RULE_dsl = 0
    RULE_create_block = 1
    RULE_create_bot = 2
    RULE_states = 3
    RULE_dataset = 4

    ruleNames =  [ "dsl", "create_block", "create_bot", "states", "dataset" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    BOT_TYPE=6
    FILE_TYPE=7
    STATE=8
    PRIORIDADE=9
    STRING=10
    NEWLINE=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class DslContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def create_block(self):
            return self.getTypedRuleContext(gramaticaParser.Create_blockContext,0)


        def states(self):
            return self.getTypedRuleContext(gramaticaParser.StatesContext,0)


        def EOF(self):
            return self.getToken(gramaticaParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.NEWLINE)
            else:
                return self.getToken(gramaticaParser.NEWLINE, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_dsl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDsl" ):
                listener.enterDsl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDsl" ):
                listener.exitDsl(self)




    def dsl(self):

        localctx = gramaticaParser.DslContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_dsl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.create_block()
            self.state = 12 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 11
                self.match(gramaticaParser.NEWLINE)
                self.state = 14 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==gramaticaParser.NEWLINE):
                    break

            self.state = 16
            self.states()
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==gramaticaParser.NEWLINE:
                self.state = 17
                self.match(gramaticaParser.NEWLINE)
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 23
            self.match(gramaticaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Create_blockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def create_bot(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.Create_botContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.Create_botContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.NEWLINE)
            else:
                return self.getToken(gramaticaParser.NEWLINE, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_create_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreate_block" ):
                listener.enterCreate_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreate_block" ):
                listener.exitCreate_block(self)




    def create_block(self):

        localctx = gramaticaParser.Create_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_create_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 25
                self.create_bot()
                self.state = 26
                self.match(gramaticaParser.NEWLINE)
                self.state = 30 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==gramaticaParser.PRIORIDADE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Create_botContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRIORIDADE(self):
            return self.getToken(gramaticaParser.PRIORIDADE, 0)

        def BOT_TYPE(self):
            return self.getToken(gramaticaParser.BOT_TYPE, 0)

        def dataset(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.DatasetContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.DatasetContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_create_bot

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreate_bot" ):
                listener.enterCreate_bot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreate_bot" ):
                listener.exitCreate_bot(self)




    def create_bot(self):

        localctx = gramaticaParser.Create_botContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_create_bot)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(gramaticaParser.PRIORIDADE)
            self.state = 33
            self.match(gramaticaParser.T__0)
            self.state = 34
            self.match(gramaticaParser.BOT_TYPE)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==gramaticaParser.T__1:
                self.state = 35
                self.match(gramaticaParser.T__1)
                self.state = 36
                self.dataset()


            self.state = 39
            self.match(gramaticaParser.T__2)
            self.state = 40
            self.dataset()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATE(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.STATE)
            else:
                return self.getToken(gramaticaParser.STATE, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_states

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStates" ):
                listener.enterStates(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStates" ):
                listener.exitStates(self)




    def states(self):

        localctx = gramaticaParser.StatesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_states)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(gramaticaParser.T__3)
            self.state = 44 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 43
                self.match(gramaticaParser.STATE)
                self.state = 46 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==gramaticaParser.STATE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DatasetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(gramaticaParser.STRING, 0)

        def FILE_TYPE(self):
            return self.getToken(gramaticaParser.FILE_TYPE, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_dataset

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataset" ):
                listener.enterDataset(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataset" ):
                listener.exitDataset(self)




    def dataset(self):

        localctx = gramaticaParser.DatasetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dataset)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(gramaticaParser.STRING)
            self.state = 49
            self.match(gramaticaParser.T__4)
            self.state = 50
            self.match(gramaticaParser.FILE_TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





