(function(a){function c(a){return typeof a=="object"?a:{top:a,left:a}}var b=a.scrollTo=function(b,c,d){a(window).scrollTo(b,c,d)};b.defaults={axis:"xy",duration:parseFloat(a.fn.jquery)>=1.3?0:1};b.window=function(b){return a(window).scrollable()};a.fn.scrollable=function(){return this.map(function(){var b=this,c=!b.nodeName||a.inArray(b.nodeName.toLowerCase(),["iframe","#document","html","body"])!=-1;if(!c)return b;var d=(b.contentWindow||b).document||b.ownerDocument||b;return a.browser.safari||d.compatMode=="BackCompat"?d.body:d.documentElement})};a.fn.scrollTo=function(d,e,f){if(typeof e=="object"){f=e;e=0}if(typeof f=="function")f={onAfter:f};if(d=="max")d=9e9;f=a.extend({},b.defaults,f);e=e||f.speed||f.duration;f.queue=f.queue&&f.axis.length>1;if(f.queue)e/=2;f.offset=c(f.offset);f.over=c(f.over);return this.scrollable().each(function(){function m(a){var c="scroll"+a;if(!k)return b[c];var d="client"+a,e=b.ownerDocument.documentElement,f=b.ownerDocument.body;return Math.max(e[c],f[c])-Math.min(e[d],f[d])}function l(a){g.animate(j,e,f.easing,a&&function(){a.call(this,d,f)})}var b=this,g=a(b),h=d,i,j={},k=g.is("html,body");switch(typeof h){case"number":case"string":if(/^([+-]=)?\d+(\.\d+)?(px)?$/.test(h)){h=c(h);break}h=a(h,this);case"object":if(h.is||h.style)i=(h=a(h)).offset()}a.each(f.axis.split(""),function(a,c){var d=c=="x"?"Left":"Top",e=d.toLowerCase(),n="scroll"+d,o=b[n],p=c=="x"?"Width":"Height";if(i){j[n]=i[e]+(k?0:o-g.offset()[e]);if(f.margin){j[n]-=parseInt(h.css("margin"+d))||0;j[n]-=parseInt(h.css("border"+d+"Width"))||0}j[n]+=f.offset[e]||0;if(f.over[e])j[n]+=h[p.toLowerCase()]()*f.over[e]}else j[n]=h[e];if(/^\d+$/.test(j[n]))j[n]=j[n]<=0?0:Math.min(j[n],m(p));if(!a&&f.queue){if(o!=j[n])l(f.onAfterFirst);delete j[n]}});l(f.onAfter);}).end()};})(jQuery)