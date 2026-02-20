+++
title = "Exorcising Big Tech: The Web Browser"
authors = ["Dom Ford"]
date = 2026-02-20T15:00:00Z
description = "My futile attempt to rid my life of big tech."
draft = false

[taxonomies]
tags = ["big tech","enshittification","technofeudalism","web browser","Google","Chrome","Chromium","Mozilla","Firefox"]


[extra]
show_copyright = true
show_comments = true
show_shares = true
show_toc = true
keywords = "big tech,enshittification,technofeudalism,Google,Chrome,Chromium,Mozilla,Firefox"
title_html = "Exorcising Big Tech: The Web Browser"
+++
> *This is the fifth of my blog posts detailing how I am and have been trying to remove big tech from my life. Read the introductory post first: [Exorcising Big Tech](/posts/exorcising-big-tech). Also check out my posts on switching [operating systems](/posts/exorcising-operating-system), [office suites](/posts/exorcising-office-suite). and [reference managers](/posts/exorcising-reference-manager).*

> **My bottom line**: For me, the best combination of ethics, features and stability is [Firefox](https://www.firefox.com/en-US/). But if you want something more similar to Chrome, go for a ‘degoogled’ Chromium-based browser like [ungoogled-chromium](https://ungoogled-software.github.io/).

***

[Google Chrome](https://www.google.com/chrome/) is *nearly* – but technically not quite – a monopoly in the web browser space. They missed out on the trifecta, as [in 2024 they *were* ruled to hold a monopoly in only two spaces](https://arstechnica.com/tech-policy/2024/08/google-loses-dojs-big-monopoly-trial-over-search-business/): internet search and text advertising. Google were given a stay of execution with Chrome, however, [when they were not forced to sell it](https://arstechnica.com/gadgets/2025/09/google-wont-have-to-sell-chrome-judge-rules/).

<div class="centered">{{ display_image(path="static/images/chrome-market-share.png", width=1000, op="fit_width") }}

*Source: [https://www.statista.com/chart/1438/browser-market-share-since-2008/](https://www.statista.com/chart/1438/browser-market-share-since-2008/)*</div>

Nonetheless, Chrome is the big beast here. It hovers over 60% of market share, having eaten away at the previous dominance of Internet Explorer (now-defunct) and [Firefox](https://www.firefox.com/en-US/). [Safari](https://www.apple.com/safari/) still maintains a respectable share, owing to its predominance on Apple machines.

# The dominance of Google Chrome and Chromium
But that’s not the whole story. Chrome itself is based on [Chromium](https://www.chromium.org/getting-involved/download-chromium/), a free, open-source web browser primarily developed by Google. Importantly, Chromium is also the foundation for many other popular web browsers, including [Microsoft Edge](https://www.microsoft.com/en-us/edge/), [Amazon Silk](https://www.amazon.com/Amazon-com-Amazon-Silk-Web-Browser/dp/B01M35MQV4) (mainly used for the the Amazon Fire line of tablets and TV players), [DuckDuckGo](https://duckduckgo.com/), [Opera](https://www.opera.com/download), [Samsung Internet](https://browser.samsung.com/beta) (mainly used on Samsung devices), [Vivaldi](https://vivaldi.com/download/), [Yandex](https://browser.yandex.com/), and [Brave](https://brave.com/download/). Chromium is *also* used for the [Electron](https://www.electronjs.org/) framework, on which [many desktop apps are now built](https://en.wikipedia.org/wiki/List_of_software_using_Electron), like GitHub Desktop, Discord, Slack, WhatsApp, Twitch, Mattermost, Notion and Obsidian.

In other words, Google’s reach extends *far*, much further than even the dominant market share of Chrome would suggest. The key question here, before we consider our choice of browser, is whether and to what extent *Chromium* is an issue. After all, it’s free and open source. The benefits of a Chromium-based browser are that you get a familiar browsing experience to Chrome, and most if not all of your extensions should still work just fine. The drawbacks are that [Chromium still ‘phones home’ to Google](https://www.techspot.com/news/103811-chromium-browsers-have-quietly-sending-user-information-google.html) in certain ways. Some Chromium-based browsers take steps to mitigate or eliminate the phoning home. Most notably, [ungoogled-chromium](https://github.com/ungoogled-software/ungoogled-chromium) does what its name suggests. Brave also adds in some toggles in the browser settings, allowing users to opt out of some of those features.

<div class="centered">{{ display_image(path="static/images/ungoogled-chromium.png", width=1000, op="fit_width") }}

*A freshly installed ungoogled-chromium.*</div>

The other argument against going with something Chromium, even if its fully degoogled, is about fighting Google’s market dominance. If Chrome is the most dominant web browser, and many of its biggest competitors are Chromium-based, then it’s no surprise that web development orbits Chrome like it’s the sun. Things are designed and developed for the web presuming a Chromium browser, by and large, with non-Chromium browsers being either deprioritized or ignored entirely. Even though I use Firefox, I have to keep a Chromium-based browser installed for the cases where a website is entirely broken on non-Chromium browsers. Chromium and especially Chrome’s dominance then becomes something of a self-fulfilling prophecy: of course it’s a powerful, well-featured and intuitive browser when everything is designed around it. It’s not an overall bad thing that the web has a predominant, free, open-source ‘standard’ that developers can rely on, rather than a thousand proprietary frameworks, it’s just a shame that it benefits Google so much.

# Non-Chromium browsers
So, what’s the alternative?

The biggest non-Chromium browser is Safari. Being proprietary Apple software, that’s not really an option for this project. The next down the list is Firefox. Firefox used to be massive, beaten only by Internet Explorer back in the day, but got quickly eaten up by Chrome in the 2010s. But Firefox is still alive, and, largely since [a big 2017 engine update](https://news.softpedia.com/news/mozilla-announces-quantum-a-new-browser-engine-for-firefox-509767.shtml), is having something of a resurgence, especially amongst those who want an alternative to a Google-dominated internet.

Firefox is run by [Mozilla](https://www.mozilla.org/en-US/). Technically speaking, Mozilla is an open-source software community which is *supported* by the non-profit [Mozilla Foundation](https://www.mozillafoundation.org/en/), and operates as the *for-profit* entity [The Mozilla Corporation](https://www.mozilla.org/en-US/foundation/moco/), which is wholly owned by the Mozilla Foundation and reinvests all of its profits into Mozilla projects. So it’s a little more complicated than a plucky, open-source community powered by friendship. But – as we will also see with other areas of software – a powerful, functional, robust web browser is just an incredibly difficult thing to produce and maintain, so it follows that it requires a larger, more organised structure behind it. [Mozilla is not without its controversies](https://www.businesseconomy.com/technology/mozillas-firefox-controversy-what-went-wrong/), but it is still a largely non-profit, open-source, community-focused, non-big-tech venture.

Personally, I use [Firefox Nightly](https://www.firefox.com/en-US/firefox/149.0a1/releasenotes/). The only difference compared with regular Firefox is that it gets bleeding-edge updates. It’s basically the [Arch](/posts/exorcising-operating-system) of Firefox versions. I don’t know, I just like getting shiny new updates and tinkering with software. Normal Firefox is just fine and more stable. 

<div class="centered">{{ display_image(path="static/images/firefox-nightly.png", width=1000, op="fit_width") }}

*A fresh window in my Firefox Nightly.*</div>

There are [a](https://www.zdnet.com/home-and-office/work-life/i-speed-tested-11-browsers-and-the-fastest-might-surprise-you/) [thousand](https://www.browserating.com/) [browser](https://www.cloudwards.net/fastest-browser/) [performance](https://www.tech2geek.net/fastest-web-browser-in-2025-speed-test-results-comparison/) [comparisons](https://www.pcworld.com/article/2390201/browser-speed-2024-this-is-how-fast-chrome-firefox-edge-co.html) you can find. I would say that selecting your browser based on how many milliseconds faster it can load a page is silly. The reality is that all modern browsers perform comparably well. But it can also depend on a lot of things: your machine, your extensions, how the webpage was developed, and so on. If one seems to be performing noticeably bad for you, by all means try another. I regularly use other browsers and see no real difference.

The choice for me is then mostly down to ethics and privacy. For me, that rules out Chromium-based browsers. There are other Firefox-based browsers – like [LibreWolf](https://librewolf.net/), [Zen Browser](https://zen-browser.app/), [WaterFox](https://www.waterfox.com/) and [Floorp](https://floorp.app/) – but honestly I’ve been satisfied enough with Firefox that I haven’t tried them enough to properly test them, and haven’t felt the need to. By all means check them out, however.

There is also the somewhat infamous [Tor Browser](https://www.torproject.org/download/), which uses [onion routing](https://en.wikipedia.org/wiki/Onion_routing). This makes it quite slow, but also far more private. It has its place, certainly, but is also used most notably for a lot of illegal activities. I’d only really recommend this as a day-to-day browser if you are literally on the run from a despotic government (in which case, please seek advice from someone more knowledgeable than me).

# Browser recommendation comparison
As always, here is a brief comparison based on my criteria and experience. It’s by no means exhaustive or expert, just my impressions.

## Firefox-based
*Best for most privacy-conscious, anti-Google users.*

| Software                                   | Ownership                    | Price | Open Source | Selling Point (What They Promote About Themselves)                                  | The Catch                                                                                                                               |
| ------------------------------------------ | ---------------------------- | ----- | ----------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| [Firefox](https://www.firefox.com/)        | Mozilla Corporation (USA)    | Free  | ✅           | Free, open source, run by a nonprofit, frequent updates, forum-based, quick support | Based in the US                                                                                                                         |
| [LibreWolf](https://librewolf.net/)        | Librewolf Community (global) | Free  | ✅           | Privacy- and security-focused, user freedom and customisation                       | Anti-DRM breaks a fair few websites like Netflix                                                                                        |
| [Zen Browser](https://zen-browser.app/)    | Zen Team (global)            | Free  | ✅           | Aesthetics, privacy, productivity and focus                                         | Some concerns regarding security and performance                                                                                        |
| [Waterfox](https://www.waterfox.com/)      | BrowserWorks (UK)            | Free  | ✅           | Privacy- and security-focused, user customisation, built-in encrytion, no telemetry | None that I can see – it just isn’t hugely distinct from other forks                                                                    |
| [Floorp](https://floorp.app/)              | Floorp Projects              | Free  | ✅           | Privacy- and security-focused, user customisation, sustainability                   | Some reports of bugginess and resource-hogging                                                                                          |
| [Tor Browser](https://www.torproject.org/) | The Tor Project (USA)        | Free  | ✅           | Ultra-privacy-focused                                                               | Slower internet speeds due to onion routing – essentially Tor is the nuclear option for privacy, at the cost of speed and functionality |
## Chromium-based
*Best for those who want a close-to-Chrome experience and/or have essential extensions only available on Chromium-based browsers.*

| Software                                                    | Ownership                     | Price | Open Source | Selling Point (What They Promote About Themselves)               | The Catch                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------------------------------- | ----------------------------- | ----- | ----------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [ungoogled-chromium](https://ungoogled-software.github.io/) | ungoogled-software (?)        | Free  | ✅           | As close to Chromium as possible, with Google surgically removed | Lacks the features of many other browsers (for some, this is an advantage)                                                                                                                                                                                                                                                         |
| [Brave](https://brave.com/download/)                        | Brave Software (US)           | Free  | ✅           | Built-in ad and tracker blocking, built-in crypto wallet         | Ethically dodgy connections now and in the past, including [cryptocurrency](https://www.pcmag.com/how-to/how-to-earn-and-use-cryptocurrency-with-the-brave-browser), [rewards](https://finance.yahoo.com/news/prominent-youtuber-claims-brave-bat-095126650.html), [ads and politics](https://www.spacebar.news/stop-using-brave-browser/) |
| [Vivaldi](https://vivaldi.com/)                             | Vivaldi Technologies (Norway) | Free  | ❌           | Not big tech, mission-oriented                                   | Some complain of a focus on features over function, with it being left a little buggy                                                                                                                                                                                                                                                      |
| [DuckDuckGo](https://duckduckgo.com/)                       | Duck Duck Go (US)             | Free  | ❌           | Privacy- and security-focused, anti-data-collection              | Mission is a little compromised by [secret deals with Microsoft](https://www.techradar.com/news/duckduckgo-in-hot-water-over-hidden-tracking-agreement-with-microsoft)                                                                                                                                                                     |
## Other
*For the true hipsters. Or those who mistrust Mozilla.*

| Software                                | Ownership                        | Price | Open Source | Selling Point (What They Promote About Themselves)     | The Catch                                     |
| --------------------------------------- | -------------------------------- | ----- | ----------- | ------------------------------------------------------ | --------------------------------------------- |
| [Pale Moon](https://www.palemoon.org/)* | Moonchild Productions (Sweden)   | Free  | ✅           | Free, open source, privacy-focused, user customisation | Dated UI, limited extensions                  |
| [Ladybird](https://ladybird.org/)       | Ladybird Browser Initiative (US) | Free  | ✅           | Privacy, customisation                                 | Not actually out yet. Looks promising though! |

\**Pale Moon is technically a Firefox fork, but that was back in 2009, so it’s as much a Firefox fork as Firefox is a Netscape fork.*

# Closing thoughts
The web browser is one of the easier pieces of software to exorcise Big Tech from. There are multiple viable paths to choose. The two most common will be either a Chromium-based, non-Google alternative, or Firefox (or derivative). The former has the advantage of being familiar and compatible if you’re coming from Chrome. The latter is a bit further from Google and helps to break its monopoly.

If you have problems with both Google and Mozilla, there are more options yet, though I really have very little experience with them.

In any case, it’s usually quite easy to port data like bookmarks over to new browsers – extensions too if you’re staying within the same ecosystem, like Chromium – so it should feel quite seamless. You’ll need to decide on your priorities and your needs. How private do you want to be? What extensions are vital to you, and which browsers support them or have equivalents?

My main recommendation is that I’ve been very happy on Firefox Nightly. It’s a good combination of privacy-focused, but also backed by a larger nonprofit organisation, which is good for long-term support and security. But this is really a space where you have a lot of options.