# Generated from gramatica.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write("I\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\6\2\22\n\2\r\2\16\2\23\3\2\3\2\3\2\6\2\31\n\2")
        buf.write("\r\2\16\2\32\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3%\n\3")
        buf.write("\3\3\3\3\3\3\6\3*\n\3\r\3\16\3+\3\4\3\4\6\4\60\n\4\r\4")
        buf.write("\16\4\61\3\5\3\5\6\5\66\n\5\r\5\16\5\67\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\5\6@\n\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\2")
        buf.write("\2\t\2\4\6\b\n\f\16\2\2\2H\2\21\3\2\2\2\4\36\3\2\2\2\6")
        buf.write("-\3\2\2\2\b\63\3\2\2\2\n?\3\2\2\2\fA\3\2\2\2\16D\3\2\2")
        buf.write("\2\20\22\5\4\3\2\21\20\3\2\2\2\22\23\3\2\2\2\23\21\3\2")
        buf.write("\2\2\23\24\3\2\2\2\24\25\3\2\2\2\25\26\7\22\2\2\26\30")
        buf.write("\5\6\4\2\27\31\7\22\2\2\30\27\3\2\2\2\31\32\3\2\2\2\32")
        buf.write("\30\3\2\2\2\32\33\3\2\2\2\33\34\3\2\2\2\34\35\5\b\5\2")
        buf.write("\35\3\3\2\2\2\36\37\7\17\2\2\37 \7\3\2\2 !\7\4\2\2!$\7")
        buf.write("\f\2\2\"#\7\5\2\2#%\5\16\b\2$\"\3\2\2\2$%\3\2\2\2%&\3")
        buf.write("\2\2\2&\'\7\6\2\2\')\5\16\b\2(*\7\22\2\2)(\3\2\2\2*+\3")
        buf.write("\2\2\2+)\3\2\2\2+,\3\2\2\2,\5\3\2\2\2-/\7\7\2\2.\60\7")
        buf.write("\16\2\2/.\3\2\2\2\60\61\3\2\2\2\61/\3\2\2\2\61\62\3\2")
        buf.write("\2\2\62\7\3\2\2\2\63\65\7\b\2\2\64\66\5\n\6\2\65\64\3")
        buf.write("\2\2\2\66\67\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28\t\3\2")
        buf.write("\2\29:\7\17\2\2:;\5\f\7\2;<\7\t\2\2<@\3\2\2\2=>\7\17\2")
        buf.write("\2>@\5\f\7\2?9\3\2\2\2?=\3\2\2\2@\13\3\2\2\2AB\7\n\2\2")
        buf.write("BC\7\20\2\2C\r\3\2\2\2DE\7\21\2\2EF\7\13\2\2FG\7\r\2\2")
        buf.write("G\17\3\2\2\2\t\23\32$+\61\67?")
        return buf.getvalue()


class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'CREATE'", "'WITH'", "'FROM'", 
                     "'STATES'", "'JOIN'", "'+'", "'!'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "BOT", "FILE_TYPE", "STATE", 
                      "BOT_NAME", "PRIORIDADE", "STRING", "NEWLINE", "WS" ]

    RULE_dsl = 0
    RULE_create = 1
    RULE_states = 2
    RULE_join = 3
    RULE_bot = 4
    RULE_prioridade_bot = 5
    RULE_dataset = 6

    ruleNames =  [ "dsl", "create", "states", "join", "bot", "prioridade_bot", 
                   "dataset" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    BOT=10
    FILE_TYPE=11
    STATE=12
    BOT_NAME=13
    PRIORIDADE=14
    STRING=15
    NEWLINE=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class DslContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.NEWLINE)
            else:
                return self.getToken(gramaticaParser.NEWLINE, i)

        def states(self):
            return self.getTypedRuleContext(gramaticaParser.StatesContext,0)


        def join(self):
            return self.getTypedRuleContext(gramaticaParser.JoinContext,0)


        def create(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.CreateContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.CreateContext,i)


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
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.create()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==gramaticaParser.BOT_NAME):
                    break

            self.state = 19
            self.match(gramaticaParser.NEWLINE)
            self.state = 20
            self.states()
            self.state = 22 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 21
                self.match(gramaticaParser.NEWLINE)
                self.state = 24 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==gramaticaParser.NEWLINE):
                    break

            self.state = 26
            self.join()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CreateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOT_NAME(self):
            return self.getToken(gramaticaParser.BOT_NAME, 0)

        def BOT(self):
            return self.getToken(gramaticaParser.BOT, 0)

        def dataset(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.DatasetContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.DatasetContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.NEWLINE)
            else:
                return self.getToken(gramaticaParser.NEWLINE, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_create

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreate" ):
                listener.enterCreate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreate" ):
                listener.exitCreate(self)




    def create(self):

        localctx = gramaticaParser.CreateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_create)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(gramaticaParser.BOT_NAME)
            self.state = 29
            self.match(gramaticaParser.T__0)
            self.state = 30
            self.match(gramaticaParser.T__1)
            self.state = 31
            self.match(gramaticaParser.BOT)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==gramaticaParser.T__2:
                self.state = 32
                self.match(gramaticaParser.T__2)
                self.state = 33
                self.dataset()


            self.state = 36
            self.match(gramaticaParser.T__3)
            self.state = 37
            self.dataset()
            self.state = 39 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 38
                    self.match(gramaticaParser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 41 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
        self.enterRule(localctx, 4, self.RULE_states)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(gramaticaParser.T__4)
            self.state = 45 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 44
                self.match(gramaticaParser.STATE)
                self.state = 47 
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

    class JoinContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bot(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.BotContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.BotContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_join

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoin" ):
                listener.enterJoin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoin" ):
                listener.exitJoin(self)




    def join(self):

        localctx = gramaticaParser.JoinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_join)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(gramaticaParser.T__5)
            self.state = 51 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 50
                self.bot()
                self.state = 53 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==gramaticaParser.BOT_NAME):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BotContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOT_NAME(self):
            return self.getToken(gramaticaParser.BOT_NAME, 0)

        def prioridade_bot(self):
            return self.getTypedRuleContext(gramaticaParser.Prioridade_botContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_bot

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBot" ):
                listener.enterBot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBot" ):
                listener.exitBot(self)




    def bot(self):

        localctx = gramaticaParser.BotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_bot)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.match(gramaticaParser.BOT_NAME)
                self.state = 56
                self.prioridade_bot()
                self.state = 57
                self.match(gramaticaParser.T__6)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.match(gramaticaParser.BOT_NAME)
                self.state = 60
                self.prioridade_bot()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Prioridade_botContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRIORIDADE(self):
            return self.getToken(gramaticaParser.PRIORIDADE, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_prioridade_bot

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrioridade_bot" ):
                listener.enterPrioridade_bot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrioridade_bot" ):
                listener.exitPrioridade_bot(self)




    def prioridade_bot(self):

        localctx = gramaticaParser.Prioridade_botContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_prioridade_bot)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(gramaticaParser.T__7)
            self.state = 64
            self.match(gramaticaParser.PRIORIDADE)
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
        self.enterRule(localctx, 12, self.RULE_dataset)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(gramaticaParser.STRING)
            self.state = 67
            self.match(gramaticaParser.T__8)
            self.state = 68
            self.match(gramaticaParser.FILE_TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





