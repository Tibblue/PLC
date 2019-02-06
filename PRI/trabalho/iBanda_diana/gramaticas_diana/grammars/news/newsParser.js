// Generated from news.g4 by ANTLR 4.5.1
// jshint ignore: start
var antlr4 = require('antlr4/index');
var newsListener = require('./newsListener').newsListener;
var grammarFileName = "news.g4";

var serializedATN = ["\u0003\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd",
    "\u0003\u000eb\u0004\u0002\t\u0002\u0004\u0003\t\u0003\u0004\u0004\t",
    "\u0004\u0004\u0005\t\u0005\u0004\u0006\t\u0006\u0004\u0007\t\u0007\u0004",
    "\b\t\b\u0004\t\t\t\u0004\n\t\n\u0004\u000b\t\u000b\u0003\u0002\u0003",
    "\u0002\u0003\u0002\u0003\u0002\u0003\u0002\u0006\u0002\u001c\n\u0002",
    "\r\u0002\u000e\u0002\u001d\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0005\u0003$\n\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0005\u0003+\n\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0004\u0003\u0004\u0003\u0004\u0003\u0004\u0003\u0004\u0003\u0004\u0005",
    "\u00045\n\u0004\u0003\u0004\u0003\u0004\u0003\u0005\u0003\u0005\u0003",
    "\u0005\u0003\u0006\u0003\u0006\u0003\u0006\u0003\u0006\u0003\u0006\u0003",
    "\u0006\u0003\u0006\u0007\u0006C\n\u0006\f\u0006\u000e\u0006F\u000b\u0006",
    "\u0003\u0007\u0003\u0007\u0003\u0007\u0003\b\u0003\b\u0003\b\u0003\b",
    "\u0003\t\u0003\t\u0003\t\u0003\t\u0003\n\u0003\n\u0003\n\u0003\n\u0003",
    "\n\u0003\n\u0003\n\u0007\nZ\n\n\f\n\u000e\n]\u000b\n\u0003\u000b\u0003",
    "\u000b\u0003\u000b\u0003\u000b\u0002\u0002\f\u0002\u0004\u0006\b\n\f",
    "\u000e\u0010\u0012\u0014\u0002\u0002]\u0002\u0016\u0003\u0002\u0002",
    "\u0002\u0004\u001f\u0003\u0002\u0002\u0002\u0006.\u0003\u0002\u0002",
    "\u0002\b8\u0003\u0002\u0002\u0002\n;\u0003\u0002\u0002\u0002\fG\u0003",
    "\u0002\u0002\u0002\u000eJ\u0003\u0002\u0002\u0002\u0010N\u0003\u0002",
    "\u0002\u0002\u0012R\u0003\u0002\u0002\u0002\u0014^\u0003\u0002\u0002",
    "\u0002\u0016\u001b\u0007\u0003\u0002\u0002\u0017\u0018\u0005\u0004\u0003",
    "\u0002\u0018\u0019\b\u0002\u0001\u0002\u0019\u001a\u0007\u0004\u0002",
    "\u0002\u001a\u001c\u0003\u0002\u0002\u0002\u001b\u0017\u0003\u0002\u0002",
    "\u0002\u001c\u001d\u0003\u0002\u0002\u0002\u001d\u001b\u0003\u0002\u0002",
    "\u0002\u001d\u001e\u0003\u0002\u0002\u0002\u001e\u0003\u0003\u0002\u0002",
    "\u0002\u001f#\u0005\u0006\u0004\u0002 !\u0005\n\u0006\u0002!\"\b\u0003",
    "\u0001\u0002\"$\u0003\u0002\u0002\u0002# \u0003\u0002\u0002\u0002#$",
    "\u0003\u0002\u0002\u0002$%\u0003\u0002\u0002\u0002%&\u0005\u000e\b\u0002",
    "&*\u0005\u0010\t\u0002\'(\u0005\u0012\n\u0002()\b\u0003\u0001\u0002",
    ")+\u0003\u0002\u0002\u0002*\'\u0003\u0002\u0002\u0002*+\u0003\u0002",
    "\u0002\u0002+,\u0003\u0002\u0002\u0002,-\b\u0003\u0001\u0002-\u0005",
    "\u0003\u0002\u0002\u0002./\u0007\u0005\u0002\u0002/4\u0005\b\u0005\u0002",
    "01\u0007\u0006\u0002\u000212\u0005\b\u0005\u000223\b\u0004\u0001\u0002",
    "35\u0003\u0002\u0002\u000240\u0003\u0002\u0002\u000245\u0003\u0002\u0002",
    "\u000256\u0003\u0002\u0002\u000267\b\u0004\u0001\u00027\u0007\u0003",
    "\u0002\u0002\u000289\u0007\f\u0002\u00029:\b\u0005\u0001\u0002:\t\u0003",
    "\u0002\u0002\u0002;<\u0007\u0007\u0002\u0002<=\u0005\f\u0007\u0002=",
    "D\b\u0006\u0001\u0002>?\u0007\b\u0002\u0002?@\u0005\f\u0007\u0002@A",
    "\b\u0006\u0001\u0002AC\u0003\u0002\u0002\u0002B>\u0003\u0002\u0002\u0002",
    "CF\u0003\u0002\u0002\u0002DB\u0003\u0002\u0002\u0002DE\u0003\u0002\u0002",
    "\u0002E\u000b\u0003\u0002\u0002\u0002FD\u0003\u0002\u0002\u0002GH\u0007",
    "\f\u0002\u0002HI\b\u0007\u0001\u0002I\r\u0003\u0002\u0002\u0002JK\u0007",
    "\t\u0002\u0002KL\u0007\f\u0002\u0002LM\b\b\u0001\u0002M\u000f\u0003",
    "\u0002\u0002\u0002NO\u0007\n\u0002\u0002OP\u0007\r\u0002\u0002PQ\b\t",
    "\u0001\u0002Q\u0011\u0003\u0002\u0002\u0002RS\u0007\u000b\u0002\u0002",
    "ST\u0005\u0014\u000b\u0002T[\b\n\u0001\u0002UV\u0007\b\u0002\u0002V",
    "W\u0005\u0014\u000b\u0002WX\b\n\u0001\u0002XZ\u0003\u0002\u0002\u0002",
    "YU\u0003\u0002\u0002\u0002Z]\u0003\u0002\u0002\u0002[Y\u0003\u0002\u0002",
    "\u0002[\\\u0003\u0002\u0002\u0002\\\u0013\u0003\u0002\u0002\u0002][",
    "\u0003\u0002\u0002\u0002^_\u0007\f\u0002\u0002_`\b\u000b\u0001\u0002",
    "`\u0015\u0003\u0002\u0002\u0002\b\u001d#*4D["].join("");


var atn = new antlr4.atn.ATNDeserializer().deserialize(serializedATN);

var decisionsToDFA = atn.decisionToState.map( function(ds, index) { return new antlr4.dfa.DFA(ds, index); });

var sharedContextCache = new antlr4.PredictionContextCache();

var literalNames = [ null, "'NEWS:'", "';'", "'TITLE:'", "'SUBTITLE:'", 
                     "'TOPICS:'", "','", "'BODY:'", "'DATE:'", "'AUTHORS:'" ];

var symbolicNames = [ null, null, null, null, null, null, null, null, null, 
                      null, "TEXT", "DATE", "Separator" ];

var ruleNames =  [ "newspaper", "news", "titles", "title", "topics", "topic", 
                   "body", "date", "authors", "author" ];

function newsParser (input) {
	antlr4.Parser.call(this, input);
    this._interp = new antlr4.atn.ParserATNSimulator(this, atn, decisionsToDFA, sharedContextCache);
    this.ruleNames = ruleNames;
    this.literalNames = literalNames;
    this.symbolicNames = symbolicNames;
    return this;
}

newsParser.prototype = Object.create(antlr4.Parser.prototype);
newsParser.prototype.constructor = newsParser;

Object.defineProperty(newsParser.prototype, "atn", {
	get : function() {
		return atn;
	}
});

newsParser.EOF = antlr4.Token.EOF;
newsParser.T__0 = 1;
newsParser.T__1 = 2;
newsParser.T__2 = 3;
newsParser.T__3 = 4;
newsParser.T__4 = 5;
newsParser.T__5 = 6;
newsParser.T__6 = 7;
newsParser.T__7 = 8;
newsParser.T__8 = 9;
newsParser.TEXT = 10;
newsParser.DATE = 11;
newsParser.Separator = 12;

newsParser.RULE_newspaper = 0;
newsParser.RULE_news = 1;
newsParser.RULE_titles = 2;
newsParser.RULE_title = 3;
newsParser.RULE_topics = 4;
newsParser.RULE_topic = 5;
newsParser.RULE_body = 6;
newsParser.RULE_date = 7;
newsParser.RULE_authors = 8;
newsParser.RULE_author = 9;

function NewspaperContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = newsParser.RULE_newspaper;
    this.val = null
    this.errors = null
    this._news = null; // NewsContext
    return this;
}

NewspaperContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
NewspaperContext.prototype.constructor = NewspaperContext;

NewspaperContext.prototype.news = function(i) {
    if(i===undefined) {
        i = null;
    }
    if(i===null) {
        return this.getTypedRuleContexts(NewsContext);
    } else {
        return this.getTypedRuleContext(NewsContext,i);
    }
};

NewspaperContext.prototype.enterRule = function(listener) {
    if(listener instanceof newsListener ) {
        listener.enterNewspaper(this);
	}
};

NewspaperContext.prototype.exitRule = function(listener) {
    if(listener instanceof newsListener ) {
        listener.exitNewspaper(this);
	}
};




newsParser.NewspaperContext = NewspaperContext;

newsParser.prototype.newspaper = function() {

    var localctx = new NewspaperContext(this, this._ctx, this.state);
    this.enterRule(localctx, 0, newsParser.RULE_newspaper);

    	localctx.val = []
    	localctx.errors = []

    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 20;
        this.match(newsParser.T__0);
        this.state = 25; 
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        do {
            this.state = 21;
            localctx._news = this.news();

            			 if(localctx._news.error!="") localctx.errors.push(localctx._news.error);
            			 else localctx.val.push(localctx._news.val);
            		 
            this.state = 23;
            this.match(newsParser.T__1);
            this.state = 27; 
            this._errHandler.sync(this);
            _la = this._input.LA(1);
        } while(_la===newsParser.T__2);
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

function NewsContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = newsParser.RULE_news;
    this.val = null
    this.error = null
    this._titles = null; // TitlesContext
    this._topics = null; // TopicsContext
    this._body = null; // BodyContext
    this._date = null; // DateContext
    this._authors = null; // AuthorsContext
    return this;
}

NewsContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
NewsContext.prototype.constructor = NewsContext;

NewsContext.prototype.titles = function() {
    return this.getTypedRuleContext(TitlesContext,0);
};

NewsContext.prototype.body = function() {
    return this.getTypedRuleContext(BodyContext,0);
};

NewsContext.prototype.date = function() {
    return this.getTypedRuleContext(DateContext,0);
};

NewsContext.prototype.topics = function() {
    return this.getTypedRuleContext(TopicsContext,0);
};

NewsContext.prototype.authors = function() {
    return this.getTypedRuleContext(AuthorsContext,0);
};

NewsContext.prototype.enterRule = function(listener) {
    if(listener instanceof newsListener ) {
        listener.enterNews(this);
	}
};

NewsContext.prototype.exitRule = function(listener) {
    if(listener instanceof newsListener ) {
        listener.exitNews(this);
	}
};




newsParser.NewsContext = NewsContext;

newsParser.prototype.news = function() {

    var localctx = new NewsContext(this, this._ctx, this.state);
    this.enterRule(localctx, 2, newsParser.RULE_news);

    	function today(){
    		var today = new Date();
    		var dd = today.getDate();
    		var mm = today.getMonth() + 1; //January is 0!
    		var yyyy = today.getFullYear();

    		if (dd < 10) {
    			dd = '0' + dd;
    		}

    		if (mm < 10) {
    			mm = '0' + mm;
    		}

    		today = yyyy + '-' + mm + '-' + dd;
    		return today;
    	}
    	var existTopics = false
    	var existAuthors = false

    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 29;
        localctx._titles = this.titles();
        this.state = 33;
        _la = this._input.LA(1);
        if(_la===newsParser.T__4) {
            this.state = 30;
            localctx._topics = this.topics();
            existTopics = true
        }

        this.state = 35;
        localctx._body = this.body();
        this.state = 36;
        localctx._date = this.date();
        this.state = 40;
        _la = this._input.LA(1);
        if(_la===newsParser.T__8) {
            this.state = 37;
            localctx._authors = this.authors();
            existAuthors = true
        }


        		if(today()>=localctx._date.val){
        			localctx.val = {
        				title: localctx._titles.titleOut,
        				subtitle: localctx._titles.subtitle,
        				body: localctx._body.val,
        				date: localctx._date.val
        			}
        			if(existTopics) localctx.val.topics = localctx._topics.val
        			else localctx.val.topics = []
        			if(existAuthors) localctx.val.authors = localctx._authors.val
        			else localctx.val.authors = []
        			localctx.error = ""
        		}else{
        			localctx.val = ""
        			localctx.error = "Date is in the future on " + localctx._titles.titleOut + " article!"
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

function TitlesContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = newsParser.RULE_titles;
    this.titleOut = null
    this.subtitle = null
    this.t = null; // TitleContext
    this.s = null; // TitleContext
    return this;
}

TitlesContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
TitlesContext.prototype.constructor = TitlesContext;

TitlesContext.prototype.title = function(i) {
    if(i===undefined) {
        i = null;
    }
    if(i===null) {
        return this.getTypedRuleContexts(TitleContext);
    } else {
        return this.getTypedRuleContext(TitleContext,i);
    }
};

TitlesContext.prototype.enterRule = function(listener) {
    if(listener instanceof newsListener ) {
        listener.enterTitles(this);
	}
};

TitlesContext.prototype.exitRule = function(listener) {
    if(listener instanceof newsListener ) {
        listener.exitTitles(this);
	}
};




newsParser.TitlesContext = TitlesContext;

newsParser.prototype.titles = function() {

    var localctx = new TitlesContext(this, this._ctx, this.state);
    this.enterRule(localctx, 4, newsParser.RULE_titles);

    	var subExists = false

    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 44;
        this.match(newsParser.T__2);
        this.state = 45;
        localctx.t = this.title();
        this.state = 50;
        _la = this._input.LA(1);
        if(_la===newsParser.T__3) {
            this.state = 46;
            this.match(newsParser.T__3);
            this.state = 47;
            localctx.s = this.title();
            subExists = true
        }


        			localctx.titleOut = localctx.t.val
        			if(subExists) localctx.subtitle = localctx.s.val
        			else localctx.subtitle = ""
        		
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
    this.ruleIndex = newsParser.RULE_title;
    this.val = null
    this._TEXT = null; // Token
    return this;
}

TitleContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
TitleContext.prototype.constructor = TitleContext;

TitleContext.prototype.TEXT = function() {
    return this.getToken(newsParser.TEXT, 0);
};

TitleContext.prototype.enterRule = function(listener) {
    if(listener instanceof newsListener ) {
        listener.enterTitle(this);
	}
};

TitleContext.prototype.exitRule = function(listener) {
    if(listener instanceof newsListener ) {
        listener.exitTitle(this);
	}
};




newsParser.TitleContext = TitleContext;

newsParser.prototype.title = function() {

    var localctx = new TitleContext(this, this._ctx, this.state);
    this.enterRule(localctx, 6, newsParser.RULE_title);
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 54;
        localctx._TEXT = this.match(newsParser.TEXT);
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

function TopicsContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = newsParser.RULE_topics;
    this.val = null
    this.t1 = null; // TopicContext
    this.t2 = null; // TopicContext
    return this;
}

TopicsContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
TopicsContext.prototype.constructor = TopicsContext;

TopicsContext.prototype.topic = function(i) {
    if(i===undefined) {
        i = null;
    }
    if(i===null) {
        return this.getTypedRuleContexts(TopicContext);
    } else {
        return this.getTypedRuleContext(TopicContext,i);
    }
};

TopicsContext.prototype.enterRule = function(listener) {
    if(listener instanceof newsListener ) {
        listener.enterTopics(this);
	}
};

TopicsContext.prototype.exitRule = function(listener) {
    if(listener instanceof newsListener ) {
        listener.exitTopics(this);
	}
};




newsParser.TopicsContext = TopicsContext;

newsParser.prototype.topics = function() {

    var localctx = new TopicsContext(this, this._ctx, this.state);
    this.enterRule(localctx, 8, newsParser.RULE_topics);

    	localctx.val = []

    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 57;
        this.match(newsParser.T__4);
        this.state = 58;
        localctx.t1 = this.topic();
        localctx.val.push(localctx.t1.val)
        this.state = 66;
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        while(_la===newsParser.T__5) {
            this.state = 60;
            this.match(newsParser.T__5);
            this.state = 61;
            localctx.t2 = this.topic();
            localctx.val.push(localctx.t2.val)
            this.state = 68;
            this._errHandler.sync(this);
            _la = this._input.LA(1);
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

function TopicContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = newsParser.RULE_topic;
    this.val = null
    this._TEXT = null; // Token
    return this;
}

TopicContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
TopicContext.prototype.constructor = TopicContext;

TopicContext.prototype.TEXT = function() {
    return this.getToken(newsParser.TEXT, 0);
};

TopicContext.prototype.enterRule = function(listener) {
    if(listener instanceof newsListener ) {
        listener.enterTopic(this);
	}
};

TopicContext.prototype.exitRule = function(listener) {
    if(listener instanceof newsListener ) {
        listener.exitTopic(this);
	}
};




newsParser.TopicContext = TopicContext;

newsParser.prototype.topic = function() {

    var localctx = new TopicContext(this, this._ctx, this.state);
    this.enterRule(localctx, 10, newsParser.RULE_topic);
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 69;
        localctx._TEXT = this.match(newsParser.TEXT);
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

function BodyContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = newsParser.RULE_body;
    this.val = null
    this._TEXT = null; // Token
    return this;
}

BodyContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
BodyContext.prototype.constructor = BodyContext;

BodyContext.prototype.TEXT = function() {
    return this.getToken(newsParser.TEXT, 0);
};

BodyContext.prototype.enterRule = function(listener) {
    if(listener instanceof newsListener ) {
        listener.enterBody(this);
	}
};

BodyContext.prototype.exitRule = function(listener) {
    if(listener instanceof newsListener ) {
        listener.exitBody(this);
	}
};




newsParser.BodyContext = BodyContext;

newsParser.prototype.body = function() {

    var localctx = new BodyContext(this, this._ctx, this.state);
    this.enterRule(localctx, 12, newsParser.RULE_body);
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 72;
        this.match(newsParser.T__6);
        this.state = 73;
        localctx._TEXT = this.match(newsParser.TEXT);
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

function DateContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = newsParser.RULE_date;
    this.val = null
    this._DATE = null; // Token
    return this;
}

DateContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
DateContext.prototype.constructor = DateContext;

DateContext.prototype.DATE = function() {
    return this.getToken(newsParser.DATE, 0);
};

DateContext.prototype.enterRule = function(listener) {
    if(listener instanceof newsListener ) {
        listener.enterDate(this);
	}
};

DateContext.prototype.exitRule = function(listener) {
    if(listener instanceof newsListener ) {
        listener.exitDate(this);
	}
};




newsParser.DateContext = DateContext;

newsParser.prototype.date = function() {

    var localctx = new DateContext(this, this._ctx, this.state);
    this.enterRule(localctx, 14, newsParser.RULE_date);
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 76;
        this.match(newsParser.T__7);
        this.state = 77;
        localctx._DATE = this.match(newsParser.DATE);
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

function AuthorsContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = newsParser.RULE_authors;
    this.val = null
    this.a1 = null; // AuthorContext
    this.a2 = null; // AuthorContext
    return this;
}

AuthorsContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
AuthorsContext.prototype.constructor = AuthorsContext;

AuthorsContext.prototype.author = function(i) {
    if(i===undefined) {
        i = null;
    }
    if(i===null) {
        return this.getTypedRuleContexts(AuthorContext);
    } else {
        return this.getTypedRuleContext(AuthorContext,i);
    }
};

AuthorsContext.prototype.enterRule = function(listener) {
    if(listener instanceof newsListener ) {
        listener.enterAuthors(this);
	}
};

AuthorsContext.prototype.exitRule = function(listener) {
    if(listener instanceof newsListener ) {
        listener.exitAuthors(this);
	}
};




newsParser.AuthorsContext = AuthorsContext;

newsParser.prototype.authors = function() {

    var localctx = new AuthorsContext(this, this._ctx, this.state);
    this.enterRule(localctx, 16, newsParser.RULE_authors);

    	localctx.val = []

    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 80;
        this.match(newsParser.T__8);
        this.state = 81;
        localctx.a1 = this.author();
        localctx.val.push(localctx.a1.val)
        this.state = 89;
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        while(_la===newsParser.T__5) {
            this.state = 83;
            this.match(newsParser.T__5);
            this.state = 84;
            localctx.a2 = this.author();
            localctx.val.push(localctx.a2.val)
            this.state = 91;
            this._errHandler.sync(this);
            _la = this._input.LA(1);
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

function AuthorContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = newsParser.RULE_author;
    this.val = null
    this._TEXT = null; // Token
    return this;
}

AuthorContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
AuthorContext.prototype.constructor = AuthorContext;

AuthorContext.prototype.TEXT = function() {
    return this.getToken(newsParser.TEXT, 0);
};

AuthorContext.prototype.enterRule = function(listener) {
    if(listener instanceof newsListener ) {
        listener.enterAuthor(this);
	}
};

AuthorContext.prototype.exitRule = function(listener) {
    if(listener instanceof newsListener ) {
        listener.exitAuthor(this);
	}
};




newsParser.AuthorContext = AuthorContext;

newsParser.prototype.author = function() {

    var localctx = new AuthorContext(this, this._ctx, this.state);
    this.enterRule(localctx, 18, newsParser.RULE_author);
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 92;
        localctx._TEXT = this.match(newsParser.TEXT);
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


exports.newsParser = newsParser;
