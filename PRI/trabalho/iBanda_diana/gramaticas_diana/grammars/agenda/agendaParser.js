// Generated from agenda.g4 by ANTLR 4.5.1
// jshint ignore: start
var antlr4 = require('antlr4/index');
var agendaListener = require('./agendaListener').agendaListener;
var grammarFileName = "agenda.g4";

var serializedATN = ["\u0003\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd",
    "\u0003\rX\u0004\u0002\t\u0002\u0004\u0003\t\u0003\u0004\u0004\t\u0004",
    "\u0004\u0005\t\u0005\u0004\u0006\t\u0006\u0004\u0007\t\u0007\u0004\b",
    "\t\b\u0004\t\t\t\u0004\n\t\n\u0004\u000b\t\u000b\u0004\f\t\f\u0004\r",
    "\t\r\u0003\u0002\u0003\u0002\u0003\u0002\u0003\u0002\u0003\u0002\u0006",
    "\u0002 \n\u0002\r\u0002\u000e\u0002!\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0005\u0003(\n\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0005\u0003-\n\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0004",
    "\u0003\u0004\u0003\u0004\u0003\u0004\u0003\u0005\u0003\u0005\u0003\u0005",
    "\u0003\u0005\u0003\u0006\u0003\u0006\u0003\u0006\u0003\u0006\u0003\u0007",
    "\u0003\u0007\u0003\u0007\u0003\u0007\u0003\b\u0003\b\u0003\b\u0003\b",
    "\u0003\b\u0003\t\u0003\t\u0003\t\u0003\t\u0003\t\u0003\n\u0003\n\u0003",
    "\n\u0003\u000b\u0003\u000b\u0003\u000b\u0003\f\u0003\f\u0003\f\u0003",
    "\r\u0003\r\u0003\r\u0003\r\u0002\u0002\u000e\u0002\u0004\u0006\b\n\f",
    "\u000e\u0010\u0012\u0014\u0016\u0018\u0002\u0002N\u0002\u001a\u0003",
    "\u0002\u0002\u0002\u0004#\u0003\u0002\u0002\u0002\u00061\u0003\u0002",
    "\u0002\u0002\b5\u0003\u0002\u0002\u0002\n9\u0003\u0002\u0002\u0002\f",
    "=\u0003\u0002\u0002\u0002\u000eA\u0003\u0002\u0002\u0002\u0010F\u0003",
    "\u0002\u0002\u0002\u0012K\u0003\u0002\u0002\u0002\u0014N\u0003\u0002",
    "\u0002\u0002\u0016Q\u0003\u0002\u0002\u0002\u0018T\u0003\u0002\u0002",
    "\u0002\u001a\u001f\u0007\u0003\u0002\u0002\u001b\u001c\u0005\u0004\u0003",
    "\u0002\u001c\u001d\b\u0002\u0001\u0002\u001d\u001e\u0007\u0004\u0002",
    "\u0002\u001e \u0003\u0002\u0002\u0002\u001f\u001b\u0003\u0002\u0002",
    "\u0002 !\u0003\u0002\u0002\u0002!\u001f\u0003\u0002\u0002\u0002!\"\u0003",
    "\u0002\u0002\u0002\"\u0003\u0003\u0002\u0002\u0002#\'\u0005\u0006\u0004",
    "\u0002$%\u0005\b\u0005\u0002%&\b\u0003\u0001\u0002&(\u0003\u0002\u0002",
    "\u0002\'$\u0003\u0002\u0002\u0002\'(\u0003\u0002\u0002\u0002(,\u0003",
    "\u0002\u0002\u0002)*\u0005\n\u0006\u0002*+\b\u0003\u0001\u0002+-\u0003",
    "\u0002\u0002\u0002,)\u0003\u0002\u0002\u0002,-\u0003\u0002\u0002\u0002",
    "-.\u0003\u0002\u0002\u0002./\u0005\f\u0007\u0002/0\b\u0003\u0001\u0002",
    "0\u0005\u0003\u0002\u0002\u000212\u0007\u0005\u0002\u000223\u0007\n",
    "\u0002\u000234\b\u0004\u0001\u00024\u0007\u0003\u0002\u0002\u000256",
    "\u0007\u0006\u0002\u000267\u0007\n\u0002\u000278\b\u0005\u0001\u0002",
    "8\t\u0003\u0002\u0002\u00029:\u0007\u0007\u0002\u0002:;\u0007\n\u0002",
    "\u0002;<\b\u0006\u0001\u0002<\u000b\u0003\u0002\u0002\u0002=>\u0005",
    "\u000e\b\u0002>?\u0005\u0010\t\u0002?@\b\u0007\u0001\u0002@\r\u0003",
    "\u0002\u0002\u0002AB\u0007\b\u0002\u0002BC\u0005\u0012\n\u0002CD\u0005",
    "\u0014\u000b\u0002DE\b\b\u0001\u0002E\u000f\u0003\u0002\u0002\u0002",
    "FG\u0007\t\u0002\u0002GH\u0005\u0016\f\u0002HI\u0005\u0018\r\u0002I",
    "J\b\t\u0001\u0002J\u0011\u0003\u0002\u0002\u0002KL\u0007\u000b\u0002",
    "\u0002LM\b\n\u0001\u0002M\u0013\u0003\u0002\u0002\u0002NO\u0007\f\u0002",
    "\u0002OP\b\u000b\u0001\u0002P\u0015\u0003\u0002\u0002\u0002QR\u0007",
    "\u000b\u0002\u0002RS\b\f\u0001\u0002S\u0017\u0003\u0002\u0002\u0002",
    "TU\u0007\f\u0002\u0002UV\b\r\u0001\u0002V\u0019\u0003\u0002\u0002\u0002",
    "\u0005!\',"].join("");


var atn = new antlr4.atn.ATNDeserializer().deserialize(serializedATN);

var decisionsToDFA = atn.decisionToState.map( function(ds, index) { return new antlr4.dfa.DFA(ds, index); });

var sharedContextCache = new antlr4.PredictionContextCache();

var literalNames = [ null, "'AGENDA:'", "';'", "'TITLE:'", "'DESC:'", "'LOCAL:'", 
                     "'BEGINS:'", "'ENDS:'" ];

var symbolicNames = [ null, null, null, null, null, null, null, null, "TEXT", 
                      "DATE", "HOUR", "Separator" ];

var ruleNames =  [ "agenda", "event", "title", "desc", "local", "time", 
                   "start", "end", "startDate", "startHour", "endDate", 
                   "endHour" ];

function agendaParser (input) {
	antlr4.Parser.call(this, input);
    this._interp = new antlr4.atn.ParserATNSimulator(this, atn, decisionsToDFA, sharedContextCache);
    this.ruleNames = ruleNames;
    this.literalNames = literalNames;
    this.symbolicNames = symbolicNames;
    return this;
}

agendaParser.prototype = Object.create(antlr4.Parser.prototype);
agendaParser.prototype.constructor = agendaParser;

Object.defineProperty(agendaParser.prototype, "atn", {
	get : function() {
		return atn;
	}
});

agendaParser.EOF = antlr4.Token.EOF;
agendaParser.T__0 = 1;
agendaParser.T__1 = 2;
agendaParser.T__2 = 3;
agendaParser.T__3 = 4;
agendaParser.T__4 = 5;
agendaParser.T__5 = 6;
agendaParser.T__6 = 7;
agendaParser.TEXT = 8;
agendaParser.DATE = 9;
agendaParser.HOUR = 10;
agendaParser.Separator = 11;

agendaParser.RULE_agenda = 0;
agendaParser.RULE_event = 1;
agendaParser.RULE_title = 2;
agendaParser.RULE_desc = 3;
agendaParser.RULE_local = 4;
agendaParser.RULE_time = 5;
agendaParser.RULE_start = 6;
agendaParser.RULE_end = 7;
agendaParser.RULE_startDate = 8;
agendaParser.RULE_startHour = 9;
agendaParser.RULE_endDate = 10;
agendaParser.RULE_endHour = 11;

function AgendaContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = agendaParser.RULE_agenda;
    this.val = null
    this.errors = null
    this._event = null; // EventContext
    return this;
}

AgendaContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
AgendaContext.prototype.constructor = AgendaContext;

AgendaContext.prototype.event = function(i) {
    if(i===undefined) {
        i = null;
    }
    if(i===null) {
        return this.getTypedRuleContexts(EventContext);
    } else {
        return this.getTypedRuleContext(EventContext,i);
    }
};

AgendaContext.prototype.enterRule = function(listener) {
    if(listener instanceof agendaListener ) {
        listener.enterAgenda(this);
	}
};

AgendaContext.prototype.exitRule = function(listener) {
    if(listener instanceof agendaListener ) {
        listener.exitAgenda(this);
	}
};




agendaParser.AgendaContext = AgendaContext;

agendaParser.prototype.agenda = function() {

    var localctx = new AgendaContext(this, this._ctx, this.state);
    this.enterRule(localctx, 0, agendaParser.RULE_agenda);

         localctx.val = []
         localctx.errors = []

    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 24;
        this.match(agendaParser.T__0);
        this.state = 29; 
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        do {
            this.state = 25;
            localctx._event = this.event();

             				if(localctx._event.error!="") localctx.errors.push(localctx._event.error);
            				else localctx.val.push(localctx._event.val);
                           
            this.state = 27;
            this.match(agendaParser.T__1);
            this.state = 31; 
            this._errHandler.sync(this);
            _la = this._input.LA(1);
        } while(_la===agendaParser.T__2);
    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};

function EventContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = agendaParser.RULE_event;
    this.val = null
    this.error = null
    this._title = null; // TitleContext
    this._desc = null; // DescContext
    this._local = null; // LocalContext
    this._time = null; // TimeContext
    return this;
}

EventContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
EventContext.prototype.constructor = EventContext;

EventContext.prototype.title = function() {
    return this.getTypedRuleContext(TitleContext,0);
};

EventContext.prototype.time = function() {
    return this.getTypedRuleContext(TimeContext,0);
};

EventContext.prototype.desc = function() {
    return this.getTypedRuleContext(DescContext,0);
};

EventContext.prototype.local = function() {
    return this.getTypedRuleContext(LocalContext,0);
};

EventContext.prototype.enterRule = function(listener) {
    if(listener instanceof agendaListener ) {
        listener.enterEvent(this);
	}
};

EventContext.prototype.exitRule = function(listener) {
    if(listener instanceof agendaListener ) {
        listener.exitEvent(this);
	}
};




agendaParser.EventContext = EventContext;

agendaParser.prototype.event = function() {

    var localctx = new EventContext(this, this._ctx, this.state);
    this.enterRule(localctx, 2, agendaParser.RULE_event);

         var existsDesc = false
         var existsLocal = false

    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 33;
        localctx._title = this.title();
        this.state = 37;
        _la = this._input.LA(1);
        if(_la===agendaParser.T__3) {
            this.state = 34;
            localctx._desc = this.desc();
            existsDesc=true
        }

        this.state = 42;
        _la = this._input.LA(1);
        if(_la===agendaParser.T__4) {
            this.state = 39;
            localctx._local = this.local();
            existsLocal=true
        }

        this.state = 44;
        localctx._time = this.time();
            
                  if(localctx._time.ts.sdate>localctx._time.te.edate){
                       localctx.val = ""
                       localctx.error = "Start date after end date on "+localctx._title.val+" event!"
                  }else{
                       if (localctx._time.ts.sdate==localctx._time.te.edate && localctx._time.ts.shour>localctx._time.te.ehour ){
                            localctx.val = ""
                            localctx.error = "Start hour after end hour on "+localctx._title.val+" event!"     
                       }else {
                            localctx.val = {
                                 title: localctx._title.val,
                                 startDate: localctx._time.ts.sdate,
                                 startHour: localctx._time.ts.shour,
                                 endDate: localctx._time.te.edate,
                                 endHour: localctx._time.te.ehour
                            }
                            if (existsDesc) localctx.val.desc = localctx._desc.val
                            else localctx.val.desc = ""
                            if (existsLocal) localctx.val.local = localctx._local.val
                            else localctx.val.local = ""
                            localctx.error = ""
                       }
                  }
             
    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};

function TitleContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = agendaParser.RULE_title;
    this.val = null
    this._TEXT = null; // Token
    return this;
}

TitleContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
TitleContext.prototype.constructor = TitleContext;

TitleContext.prototype.TEXT = function() {
    return this.getToken(agendaParser.TEXT, 0);
};

TitleContext.prototype.enterRule = function(listener) {
    if(listener instanceof agendaListener ) {
        listener.enterTitle(this);
	}
};

TitleContext.prototype.exitRule = function(listener) {
    if(listener instanceof agendaListener ) {
        listener.exitTitle(this);
	}
};




agendaParser.TitleContext = TitleContext;

agendaParser.prototype.title = function() {

    var localctx = new TitleContext(this, this._ctx, this.state);
    this.enterRule(localctx, 4, agendaParser.RULE_title);
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 47;
        this.match(agendaParser.T__2);
        this.state = 48;
        localctx._TEXT = this.match(agendaParser.TEXT);
        localctx.val = (localctx._TEXT===null ? null : localctx._TEXT.text).substring(1, (localctx._TEXT===null ? null : localctx._TEXT.text).length-1)
    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};

function DescContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = agendaParser.RULE_desc;
    this.val = null
    this._TEXT = null; // Token
    return this;
}

DescContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
DescContext.prototype.constructor = DescContext;

DescContext.prototype.TEXT = function() {
    return this.getToken(agendaParser.TEXT, 0);
};

DescContext.prototype.enterRule = function(listener) {
    if(listener instanceof agendaListener ) {
        listener.enterDesc(this);
	}
};

DescContext.prototype.exitRule = function(listener) {
    if(listener instanceof agendaListener ) {
        listener.exitDesc(this);
	}
};




agendaParser.DescContext = DescContext;

agendaParser.prototype.desc = function() {

    var localctx = new DescContext(this, this._ctx, this.state);
    this.enterRule(localctx, 6, agendaParser.RULE_desc);
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 51;
        this.match(agendaParser.T__3);
        this.state = 52;
        localctx._TEXT = this.match(agendaParser.TEXT);
        localctx.val = (localctx._TEXT===null ? null : localctx._TEXT.text).substring(1, (localctx._TEXT===null ? null : localctx._TEXT.text).length-1)
    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};

function LocalContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = agendaParser.RULE_local;
    this.val = null
    this._TEXT = null; // Token
    return this;
}

LocalContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
LocalContext.prototype.constructor = LocalContext;

LocalContext.prototype.TEXT = function() {
    return this.getToken(agendaParser.TEXT, 0);
};

LocalContext.prototype.enterRule = function(listener) {
    if(listener instanceof agendaListener ) {
        listener.enterLocal(this);
	}
};

LocalContext.prototype.exitRule = function(listener) {
    if(listener instanceof agendaListener ) {
        listener.exitLocal(this);
	}
};




agendaParser.LocalContext = LocalContext;

agendaParser.prototype.local = function() {

    var localctx = new LocalContext(this, this._ctx, this.state);
    this.enterRule(localctx, 8, agendaParser.RULE_local);
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 55;
        this.match(agendaParser.T__4);
        this.state = 56;
        localctx._TEXT = this.match(agendaParser.TEXT);
        localctx.val = (localctx._TEXT===null ? null : localctx._TEXT.text).substring(1, (localctx._TEXT===null ? null : localctx._TEXT.text).length-1)
    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};

function TimeContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = agendaParser.RULE_time;
    this.ts = null
    this.te = null
    this.s = null; // StartContext
    this.e = null; // EndContext
    return this;
}

TimeContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
TimeContext.prototype.constructor = TimeContext;

TimeContext.prototype.start = function() {
    return this.getTypedRuleContext(StartContext,0);
};

TimeContext.prototype.end = function() {
    return this.getTypedRuleContext(EndContext,0);
};

TimeContext.prototype.enterRule = function(listener) {
    if(listener instanceof agendaListener ) {
        listener.enterTime(this);
	}
};

TimeContext.prototype.exitRule = function(listener) {
    if(listener instanceof agendaListener ) {
        listener.exitTime(this);
	}
};




agendaParser.TimeContext = TimeContext;

agendaParser.prototype.time = function() {

    var localctx = new TimeContext(this, this._ctx, this.state);
    this.enterRule(localctx, 10, agendaParser.RULE_time);
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 59;
        localctx.s = this.start();
        this.state = 60;
        localctx.e = this.end();

                  localctx.ts = {
                       sdate: localctx.s.sd,
                       shour: localctx.s.sh
                  }
                  localctx.te = {
                       edate: localctx.e.ed,
                       ehour: localctx.e.eh
                  }
             
    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};

function StartContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = agendaParser.RULE_start;
    this.sd = null
    this.sh = null
    this.d = null; // StartDateContext
    this.h = null; // StartHourContext
    return this;
}

StartContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
StartContext.prototype.constructor = StartContext;

StartContext.prototype.startDate = function() {
    return this.getTypedRuleContext(StartDateContext,0);
};

StartContext.prototype.startHour = function() {
    return this.getTypedRuleContext(StartHourContext,0);
};

StartContext.prototype.enterRule = function(listener) {
    if(listener instanceof agendaListener ) {
        listener.enterStart(this);
	}
};

StartContext.prototype.exitRule = function(listener) {
    if(listener instanceof agendaListener ) {
        listener.exitStart(this);
	}
};




agendaParser.StartContext = StartContext;

agendaParser.prototype.start = function() {

    var localctx = new StartContext(this, this._ctx, this.state);
    this.enterRule(localctx, 12, agendaParser.RULE_start);
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 63;
        this.match(agendaParser.T__5);
        this.state = 64;
        localctx.d = this.startDate();
        this.state = 65;
        localctx.h = this.startHour();

                  localctx.sd = localctx.d.val
                  localctx.sh = localctx.h.val
             
    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};

function EndContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = agendaParser.RULE_end;
    this.ed = null
    this.eh = null
    this.d = null; // EndDateContext
    this.h = null; // EndHourContext
    return this;
}

EndContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
EndContext.prototype.constructor = EndContext;

EndContext.prototype.endDate = function() {
    return this.getTypedRuleContext(EndDateContext,0);
};

EndContext.prototype.endHour = function() {
    return this.getTypedRuleContext(EndHourContext,0);
};

EndContext.prototype.enterRule = function(listener) {
    if(listener instanceof agendaListener ) {
        listener.enterEnd(this);
	}
};

EndContext.prototype.exitRule = function(listener) {
    if(listener instanceof agendaListener ) {
        listener.exitEnd(this);
	}
};




agendaParser.EndContext = EndContext;

agendaParser.prototype.end = function() {

    var localctx = new EndContext(this, this._ctx, this.state);
    this.enterRule(localctx, 14, agendaParser.RULE_end);
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 68;
        this.match(agendaParser.T__6);
        this.state = 69;
        localctx.d = this.endDate();
        this.state = 70;
        localctx.h = this.endHour();

                  localctx.ed = localctx.d.val
                  localctx.eh = localctx.h.val
             
    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};

function StartDateContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = agendaParser.RULE_startDate;
    this.val = null
    this._DATE = null; // Token
    return this;
}

StartDateContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
StartDateContext.prototype.constructor = StartDateContext;

StartDateContext.prototype.DATE = function() {
    return this.getToken(agendaParser.DATE, 0);
};

StartDateContext.prototype.enterRule = function(listener) {
    if(listener instanceof agendaListener ) {
        listener.enterStartDate(this);
	}
};

StartDateContext.prototype.exitRule = function(listener) {
    if(listener instanceof agendaListener ) {
        listener.exitStartDate(this);
	}
};




agendaParser.StartDateContext = StartDateContext;

agendaParser.prototype.startDate = function() {

    var localctx = new StartDateContext(this, this._ctx, this.state);
    this.enterRule(localctx, 16, agendaParser.RULE_startDate);
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 73;
        localctx._DATE = this.match(agendaParser.DATE);
        localctx.val = (localctx._DATE===null ? null : localctx._DATE.text)
    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};

function StartHourContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = agendaParser.RULE_startHour;
    this.val = null
    this._HOUR = null; // Token
    return this;
}

StartHourContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
StartHourContext.prototype.constructor = StartHourContext;

StartHourContext.prototype.HOUR = function() {
    return this.getToken(agendaParser.HOUR, 0);
};

StartHourContext.prototype.enterRule = function(listener) {
    if(listener instanceof agendaListener ) {
        listener.enterStartHour(this);
	}
};

StartHourContext.prototype.exitRule = function(listener) {
    if(listener instanceof agendaListener ) {
        listener.exitStartHour(this);
	}
};




agendaParser.StartHourContext = StartHourContext;

agendaParser.prototype.startHour = function() {

    var localctx = new StartHourContext(this, this._ctx, this.state);
    this.enterRule(localctx, 18, agendaParser.RULE_startHour);
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 76;
        localctx._HOUR = this.match(agendaParser.HOUR);
        localctx.val = (localctx._HOUR===null ? null : localctx._HOUR.text)
    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};

function EndDateContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = agendaParser.RULE_endDate;
    this.val = null
    this._DATE = null; // Token
    return this;
}

EndDateContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
EndDateContext.prototype.constructor = EndDateContext;

EndDateContext.prototype.DATE = function() {
    return this.getToken(agendaParser.DATE, 0);
};

EndDateContext.prototype.enterRule = function(listener) {
    if(listener instanceof agendaListener ) {
        listener.enterEndDate(this);
	}
};

EndDateContext.prototype.exitRule = function(listener) {
    if(listener instanceof agendaListener ) {
        listener.exitEndDate(this);
	}
};




agendaParser.EndDateContext = EndDateContext;

agendaParser.prototype.endDate = function() {

    var localctx = new EndDateContext(this, this._ctx, this.state);
    this.enterRule(localctx, 20, agendaParser.RULE_endDate);
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 79;
        localctx._DATE = this.match(agendaParser.DATE);
        localctx.val = (localctx._DATE===null ? null : localctx._DATE.text)
    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};

function EndHourContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = agendaParser.RULE_endHour;
    this.val = null
    this._HOUR = null; // Token
    return this;
}

EndHourContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
EndHourContext.prototype.constructor = EndHourContext;

EndHourContext.prototype.HOUR = function() {
    return this.getToken(agendaParser.HOUR, 0);
};

EndHourContext.prototype.enterRule = function(listener) {
    if(listener instanceof agendaListener ) {
        listener.enterEndHour(this);
	}
};

EndHourContext.prototype.exitRule = function(listener) {
    if(listener instanceof agendaListener ) {
        listener.exitEndHour(this);
	}
};




agendaParser.EndHourContext = EndHourContext;

agendaParser.prototype.endHour = function() {

    var localctx = new EndHourContext(this, this._ctx, this.state);
    this.enterRule(localctx, 22, agendaParser.RULE_endHour);
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 82;
        localctx._HOUR = this.match(agendaParser.HOUR);
        localctx.val = (localctx._HOUR===null ? null : localctx._HOUR.text)
    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};


exports.agendaParser = agendaParser;
