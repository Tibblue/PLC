# Generated from gramatica.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\20I\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write(u"\4\b\t\b\4\t\t\t\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3\2")
        buf.write(u"\3\2\5\2\33\n\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3#\n\3\3\3")
        buf.write(u"\3\3\3\3\3\4\7\4)\n\4\f\4\16\4,\13\4\3\5\3\5\3\5\3\5")
        buf.write(u"\3\5\7\5\63\n\5\f\5\16\5\66\13\5\3\5\3\5\3\5\5\5;\n\5")
        buf.write(u"\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write(u"\2\2\n\2\4\6\b\n\f\16\20\2\2\2G\2\32\3\2\2\2\4\34\3\2")
        buf.write(u"\2\2\6*\3\2\2\2\b:\3\2\2\2\n<\3\2\2\2\f?\3\2\2\2\16B")
        buf.write(u"\3\2\2\2\20F\3\2\2\2\22\24\5\4\3\2\23\22\3\2\2\2\24\27")
        buf.write(u"\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\33\3\2\2\2\27")
        buf.write(u"\25\3\2\2\2\30\33\5\6\4\2\31\33\5\b\5\2\32\25\3\2\2\2")
        buf.write(u"\32\30\3\2\2\2\32\31\3\2\2\2\33\3\3\2\2\2\34\35\5\n\6")
        buf.write(u"\2\35\36\7\3\2\2\36\37\7\4\2\2\37\"\7\17\2\2 !\7\5\2")
        buf.write(u"\2!#\5\16\b\2\" \3\2\2\2\"#\3\2\2\2#$\3\2\2\2$%\7\6\2")
        buf.write(u"\2%&\5\16\b\2&\5\3\2\2\2\')\5\20\t\2(\'\3\2\2\2),\3\2")
        buf.write(u"\2\2*(\3\2\2\2*+\3\2\2\2+\7\3\2\2\2,*\3\2\2\2-\64\7\7")
        buf.write(u"\2\2./\5\n\6\2/\60\5\f\7\2\60\61\7\b\2\2\61\63\3\2\2")
        buf.write(u"\2\62.\3\2\2\2\63\66\3\2\2\2\64\62\3\2\2\2\64\65\3\2")
        buf.write(u"\2\2\65;\3\2\2\2\66\64\3\2\2\2\678\5\n\6\289\5\f\7\2")
        buf.write(u"9;\3\2\2\2:-\3\2\2\2:\67\3\2\2\2;\t\3\2\2\2<=\7\t\2\2")
        buf.write(u"=>\7\r\2\2>\13\3\2\2\2?@\7\n\2\2@A\7\f\2\2A\r\3\2\2\2")
        buf.write(u"BC\7\16\2\2CD\7\13\2\2DE\7\20\2\2E\17\3\2\2\2FG\7\16")
        buf.write(u"\2\2G\21\3\2\2\2\b\25\32\"*\64:")
        return buf.getvalue()


class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'='", u"'CREATE'", u"'WITH'", u"'FROM'", 
                     u"'JOIN'", u"'+'", u"'b'", u"'!'", u"'.'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"PRIORIDADE", u"NUMERO", 
                      u"STRING", u"BOT", u"FILE_TYPE" ]

    RULE_dsl = 0
    RULE_create = 1
    RULE_states = 2
    RULE_join = 3
    RULE_bot_name = 4
    RULE_prioridade_bot = 5
    RULE_dataset = 6
    RULE_estado = 7

    ruleNames =  [ u"dsl", u"create", u"states", u"join", u"bot_name", u"prioridade_bot", 
                   u"dataset", u"estado" ]

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
    PRIORIDADE=10
    NUMERO=11
    STRING=12
    BOT=13
    FILE_TYPE=14

    def __init__(self, input, output=sys.stdout):
        super(gramaticaParser, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class DslContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(gramaticaParser.DslContext, self).__init__(parent, invokingState)
            self.parser = parser

        def create(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.CreateContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.CreateContext,i)


        def states(self):
            return self.getTypedRuleContext(gramaticaParser.StatesContext,0)


        def join(self):
            return self.getTypedRuleContext(gramaticaParser.JoinContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_dsl

        def enterRule(self, listener):
            if hasattr(listener, "enterDsl"):
                listener.enterDsl(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDsl"):
                listener.exitDsl(self)




    def dsl(self):

        localctx = gramaticaParser.DslContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_dsl)
        self._la = 0 # Token type
        try:
            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==gramaticaParser.T__6:
                    self.state = 16
                    self.create()
                    self.state = 21
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.states()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.join()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CreateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(gramaticaParser.CreateContext, self).__init__(parent, invokingState)
            self.parser = parser

        def bot_name(self):
            return self.getTypedRuleContext(gramaticaParser.Bot_nameContext,0)


        def BOT(self):
            return self.getToken(gramaticaParser.BOT, 0)

        def dataset(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.DatasetContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.DatasetContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_create

        def enterRule(self, listener):
            if hasattr(listener, "enterCreate"):
                listener.enterCreate(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCreate"):
                listener.exitCreate(self)




    def create(self):

        localctx = gramaticaParser.CreateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_create)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.bot_name()
            self.state = 27
            self.match(gramaticaParser.T__0)
            self.state = 28
            self.match(gramaticaParser.T__1)
            self.state = 29
            self.match(gramaticaParser.BOT)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==gramaticaParser.T__2:
                self.state = 30
                self.match(gramaticaParser.T__2)
                self.state = 31
                self.dataset()


            self.state = 34
            self.match(gramaticaParser.T__3)
            self.state = 35
            self.dataset()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatesContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(gramaticaParser.StatesContext, self).__init__(parent, invokingState)
            self.parser = parser

        def estado(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.EstadoContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.EstadoContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_states

        def enterRule(self, listener):
            if hasattr(listener, "enterStates"):
                listener.enterStates(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitStates"):
                listener.exitStates(self)




    def states(self):

        localctx = gramaticaParser.StatesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_states)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==gramaticaParser.STRING:
                self.state = 37
                self.estado()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class JoinContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(gramaticaParser.JoinContext, self).__init__(parent, invokingState)
            self.parser = parser

        def bot_name(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.Bot_nameContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.Bot_nameContext,i)


        def prioridade_bot(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.Prioridade_botContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.Prioridade_botContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_join

        def enterRule(self, listener):
            if hasattr(listener, "enterJoin"):
                listener.enterJoin(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJoin"):
                listener.exitJoin(self)




    def join(self):

        localctx = gramaticaParser.JoinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_join)
        self._la = 0 # Token type
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [gramaticaParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.match(gramaticaParser.T__4)
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==gramaticaParser.T__6:
                    self.state = 44
                    self.bot_name()
                    self.state = 45
                    self.prioridade_bot()
                    self.state = 46
                    self.match(gramaticaParser.T__5)
                    self.state = 52
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [gramaticaParser.T__6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.bot_name()
                self.state = 54
                self.prioridade_bot()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Bot_nameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(gramaticaParser.Bot_nameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(gramaticaParser.NUMERO, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_bot_name

        def enterRule(self, listener):
            if hasattr(listener, "enterBot_name"):
                listener.enterBot_name(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBot_name"):
                listener.exitBot_name(self)




    def bot_name(self):

        localctx = gramaticaParser.Bot_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_bot_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(gramaticaParser.T__6)
            self.state = 59
            self.match(gramaticaParser.NUMERO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Prioridade_botContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(gramaticaParser.Prioridade_botContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PRIORIDADE(self):
            return self.getToken(gramaticaParser.PRIORIDADE, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_prioridade_bot

        def enterRule(self, listener):
            if hasattr(listener, "enterPrioridade_bot"):
                listener.enterPrioridade_bot(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPrioridade_bot"):
                listener.exitPrioridade_bot(self)




    def prioridade_bot(self):

        localctx = gramaticaParser.Prioridade_botContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_prioridade_bot)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(gramaticaParser.T__7)
            self.state = 62
            self.match(gramaticaParser.PRIORIDADE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DatasetContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(gramaticaParser.DatasetContext, self).__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(gramaticaParser.STRING, 0)

        def FILE_TYPE(self):
            return self.getToken(gramaticaParser.FILE_TYPE, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_dataset

        def enterRule(self, listener):
            if hasattr(listener, "enterDataset"):
                listener.enterDataset(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDataset"):
                listener.exitDataset(self)




    def dataset(self):

        localctx = gramaticaParser.DatasetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_dataset)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(gramaticaParser.STRING)
            self.state = 65
            self.match(gramaticaParser.T__8)
            self.state = 66
            self.match(gramaticaParser.FILE_TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EstadoContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(gramaticaParser.EstadoContext, self).__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(gramaticaParser.STRING, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_estado

        def enterRule(self, listener):
            if hasattr(listener, "enterEstado"):
                listener.enterEstado(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEstado"):
                listener.exitEstado(self)




    def estado(self):

        localctx = gramaticaParser.EstadoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_estado)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(gramaticaParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





