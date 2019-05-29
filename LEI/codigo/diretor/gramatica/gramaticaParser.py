# Generated from gramatica.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("T\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\6\2\25\n\2\r\2\16\2\26\3\2\3\2\6")
        buf.write("\2\33\n\2\r\2\16\2\34\3\2\3\2\7\2!\n\2\f\2\16\2$\13\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\6\3+\n\3\r\3\16\3,\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\5\4\65\n\4\3\4\3\4\3\4\3\5\3\5\6\5<\n\5\r\5")
        buf.write("\16\5=\3\6\3\6\3\6\3\7\3\7\3\7\7\7F\n\7\f\7\16\7I\13\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\2\2\n\2\4\6\b")
        buf.write("\n\f\16\20\2\3\4\2\t\t\21\21\2R\2\22\3\2\2\2\4*\3\2\2")
        buf.write("\2\6.\3\2\2\2\b9\3\2\2\2\n?\3\2\2\2\fG\3\2\2\2\16L\3\2")
        buf.write("\2\2\20O\3\2\2\2\22\24\5\4\3\2\23\25\7\21\2\2\24\23\3")
        buf.write("\2\2\2\25\26\3\2\2\2\26\24\3\2\2\2\26\27\3\2\2\2\27\30")
        buf.write("\3\2\2\2\30\32\5\b\5\2\31\33\7\21\2\2\32\31\3\2\2\2\33")
        buf.write("\34\3\2\2\2\34\32\3\2\2\2\34\35\3\2\2\2\35\36\3\2\2\2")
        buf.write("\36\"\5\n\6\2\37!\7\21\2\2 \37\3\2\2\2!$\3\2\2\2\" \3")
        buf.write("\2\2\2\"#\3\2\2\2#%\3\2\2\2$\"\3\2\2\2%&\7\2\2\3&\3\3")
        buf.write("\2\2\2\'(\5\6\4\2()\7\21\2\2)+\3\2\2\2*\'\3\2\2\2+,\3")
        buf.write("\2\2\2,*\3\2\2\2,-\3\2\2\2-\5\3\2\2\2./\7\16\2\2/\60\7")
        buf.write("\3\2\2\60\61\7\4\2\2\61\64\7\13\2\2\62\63\7\5\2\2\63\65")
        buf.write("\5\20\t\2\64\62\3\2\2\2\64\65\3\2\2\2\65\66\3\2\2\2\66")
        buf.write("\67\7\6\2\2\678\5\20\t\28\7\3\2\2\29;\7\7\2\2:<\7\r\2")
        buf.write("\2;:\3\2\2\2<=\3\2\2\2=;\3\2\2\2=>\3\2\2\2>\t\3\2\2\2")
        buf.write("?@\7\b\2\2@A\5\f\7\2A\13\3\2\2\2BC\5\16\b\2CD\t\2\2\2")
        buf.write("DF\3\2\2\2EB\3\2\2\2FI\3\2\2\2GE\3\2\2\2GH\3\2\2\2HJ\3")
        buf.write("\2\2\2IG\3\2\2\2JK\5\16\b\2K\r\3\2\2\2LM\7\16\2\2MN\7")
        buf.write("\17\2\2N\17\3\2\2\2OP\7\20\2\2PQ\7\n\2\2QR\7\f\2\2R\21")
        buf.write("\3\2\2\2\t\26\34\",\64=G")
        return buf.getvalue()


class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'CREATE'", "'WITH'", "'FROM'", 
                     "'STATES'", "'JOIN'", "'+'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "BOT_TYPE", "FILE_TYPE", "STATE", "BOT_NAME", 
                      "PRIORIDADE", "STRING", "NEWLINE", "WS" ]

    RULE_dsl = 0
    RULE_create_block = 1
    RULE_create_bot = 2
    RULE_states = 3
    RULE_join = 4
    RULE_bots = 5
    RULE_bot = 6
    RULE_dataset = 7

    ruleNames =  [ "dsl", "create_block", "create_bot", "states", "join", 
                   "bots", "bot", "dataset" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    BOT_TYPE=9
    FILE_TYPE=10
    STATE=11
    BOT_NAME=12
    PRIORIDADE=13
    STRING=14
    NEWLINE=15
    WS=16

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


        def join(self):
            return self.getTypedRuleContext(gramaticaParser.JoinContext,0)


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
            self.state = 16
            self.create_block()
            self.state = 18 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 17
                self.match(gramaticaParser.NEWLINE)
                self.state = 20 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==gramaticaParser.NEWLINE):
                    break

            self.state = 22
            self.states()
            self.state = 24 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 23
                self.match(gramaticaParser.NEWLINE)
                self.state = 26 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==gramaticaParser.NEWLINE):
                    break

            self.state = 28
            self.join()
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==gramaticaParser.NEWLINE:
                self.state = 29
                self.match(gramaticaParser.NEWLINE)
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 35
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
            self.state = 40 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 37
                self.create_bot()
                self.state = 38
                self.match(gramaticaParser.NEWLINE)
                self.state = 42 
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

    class Create_botContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOT_NAME(self):
            return self.getToken(gramaticaParser.BOT_NAME, 0)

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
            self.state = 44
            self.match(gramaticaParser.BOT_NAME)
            self.state = 45
            self.match(gramaticaParser.T__0)
            self.state = 46
            self.match(gramaticaParser.T__1)
            self.state = 47
            self.match(gramaticaParser.BOT_TYPE)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==gramaticaParser.T__2:
                self.state = 48
                self.match(gramaticaParser.T__2)
                self.state = 49
                self.dataset()


            self.state = 52
            self.match(gramaticaParser.T__3)
            self.state = 53
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
            self.state = 55
            self.match(gramaticaParser.T__4)
            self.state = 57 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 56
                self.match(gramaticaParser.STATE)
                self.state = 59 
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

        def bots(self):
            return self.getTypedRuleContext(gramaticaParser.BotsContext,0)


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
        self.enterRule(localctx, 8, self.RULE_join)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(gramaticaParser.T__5)
            self.state = 62
            self.bots()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BotsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bot(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.BotContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.BotContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.NEWLINE)
            else:
                return self.getToken(gramaticaParser.NEWLINE, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_bots

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBots" ):
                listener.enterBots(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBots" ):
                listener.exitBots(self)




    def bots(self):

        localctx = gramaticaParser.BotsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_bots)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 64
                    self.bot()
                    self.state = 65
                    _la = self._input.LA(1)
                    if not(_la==gramaticaParser.T__6 or _la==gramaticaParser.NEWLINE):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 71
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 72
            self.bot()
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

        def PRIORIDADE(self):
            return self.getToken(gramaticaParser.PRIORIDADE, 0)

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
        self.enterRule(localctx, 12, self.RULE_bot)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(gramaticaParser.BOT_NAME)
            self.state = 75
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
        self.enterRule(localctx, 14, self.RULE_dataset)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(gramaticaParser.STRING)
            self.state = 78
            self.match(gramaticaParser.T__7)
            self.state = 79
            self.match(gramaticaParser.FILE_TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





