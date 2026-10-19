+++
title = "Exorcising Big Tech: Using a VPN"
authors = ["Dom Ford"]
date = 2026-10-18T15:00:00Z
description = "My futile attempt to rid my life of big tech."
draft = false

[taxonomies]
tags = ["big tech","enshittification","technofeudalism","VPN","Mullvad","privacy","cybersecurity"]


[extra]
show_copyright = true
show_comments = true
show_shares = true
show_toc = true
keywords = "big tech,enshittification,technofeudalism,VPN,Mullvad,privacy,cybersecurity"
title_html = "Exorcising Big Tech: Using a VPN"
+++
> *This is the seventh of my blog posts detailing how I am and have been trying to remove big tech from my life. Read the introductory post first: [Exorcising Big Tech](/posts/exorcising-big-tech). Also check out my posts on [operating systems](/posts/exorcising-operating-system), [office suites](/posts/exorcising-office-suite), [reference managers](/posts/exorcising-reference-manager), [web browsers](/posts/exorcising-web-browser) and [notetaking](/posts/exorcising-notetaking).*

> **My bottom line**: Use a VPN, either intermittently or all the time. My recommendation is [Mullvad](https://mullvad.net/en), but there are many good options, so long as you *never* use a free VPN.

***

Should you use a VPN? Your favourite YouTuber certainly thinks so – or is paid to say so, at least. And what do they have to do with big tech? Rather than previous blog posts – which were about things like a web browser or an office suite that you almost certainly use – you might not use a VPN. Or you might only use it to connect to your institution’s network from home or abroad.

# What is a VPN?
VPN stands for *virtual private network*. Basically, it’s a middleman. Instead of connecting directly to a website, you connect to your VPN’s servers which *then* connect to the website, and route the data back to your device. To that end, a VPN serves two basic functions.

First, it masks your identity to the endpoint. The website or service only sees the connection from the VPN’s server, not your device which sent the original request to the VPN. That’s good for privacy and security because your machine is not identified as one of the nodes in the network, and therefore can’t* be identified or targeted. 

*<small>\* It’s not impossible, of course, just much more difficult.</small>*

Second, it makes all your web traffic seem to the endpoint like it’s coming from the VPN server. This is used for things like an institution’s VPN – so you can connect to your workplace’s network from abroad but have it treat you as if you were in the office. It can also be used to bypass certain restrictions and filters. Most popularly, streaming sites like Netflix serve content geographically. If a show you want to watch is not available on the Netflix catalogue in your country but is in another, you can connect to a VPN server based in that country to be served that catalogue. Note that this kind of usage is against Netflix’s (and pretty much every streaming platform’s) terms of service, though. They go to a lot of effort to block VPN (or suspected VPN) traffic. Technically speaking, they can ban you from the platform, but Netflix at least [has shown no signs](https://proprivacy.com/vpn/guides/illegal-vpn-netflix) of wanting to do that. This geographic advantage goes for any geographic restrictions, including political ones like [China’s ‘Great Firewall’](https://realchinaexperiences.com/2025/05/06/the-brutally-honest-guide-to-vpns-for-china-from-someone-whos-been-there/).

# Why use a VPN?
There are a few obvious use-cases there. If you’re a political dissident in an authoritarian country, you should probably already be using a VPN, and you definitely shouldn’t be looking to me for advice. If you want another country’s Netflix library, that’s another obvious use-case.

But it may also be worth using for other, less tangible reasons. Because it masks your traffic and makes it seem like it’s coming from the VPN server and not your device, this messes with pretty much everything that uses information about your device. That means targeted ads and user data gathering, for example. It gives me a warm feeling knowing that I’m doing something small to pollute user datasets with garbage data. Let’s say 500 users access a web service. Ordinarily, they would get data on each of these 500 users, which device they used, when they accessed the site, where they live, and [a plethora of information](https://kuber.studio/cookie/). If those 500 users all used the same VPN, the website would instead get 500 connections of unknown origin from a set of (probably known) VPN servers. There’s still plenty they do know about those 500 users – from the machine they use to whether or not you’re using a mouse – but it’s *something*.

Many VPNs also have some additional features that are *really* useful. My choice, [Mullvad](https://mullvad.net/en), offers ‘DNS content blockers’, which allow you to block your choice of ads, trackers, malware, gambling, adult content and social media at the DNS level. It works differently to a browser-based ad-blocker, and so the two are best used together. Essentially, it takes the known DNSes of ad servers and refuses to resolve them, meaning the ads (or whichever of the options you choose) never reach your device in the first place.

I also make use of ‘split tunnelling’. This is a feature to open specific apps without routing its traffic through the VPN but without turning the VPN off entirely. This can use very helpful for some of the reasons I’m about to go through.

# The downsides
Apart from costing money ([do *not* ever use a ‘free’ VPN](https://www.howtogeek.com/the-truth-behind-free-vpns-and-why-you-couldnt-pay-me-to-use-one/)), there are a few drawbacks to using a VPN to be aware of.

- **Every website thinks you’re a bot:** Do you like doing CAPTCHAs? Using a VPN significantly increases the likelihood that a web service sees your traffic as ‘suspicious’ and requires you to prove you’re not a robot. Whether this is good faith security or maliciously nudging you away from using VPNs so they can get their hands on your delicious data, it’s a reality of using the internet with a VPN.

- **Some services don’t like VPNs:** Some go so far as to block you entirely. It’s a constant game of cat and mouse, because VPNs only have so many servers and many users route through them, their IP addresses become known fairly quickly even when they change. Many websites will put specific counter-VPN measures in place with this knowledge. For example, I cannot access BBC iPlayer when I VPN to the UK, because it detects that I am using a VPN and blocks me. *Old School RuneScape*’s launcher won’t let me log in while using a VPN.

- **Speed:** This is rarely an issue with a good VPN service, but it can come up. Because you’re routing your internet traffic less directly, through a middleman, it is inherently slower. With a good VPN, it is almost never noticeable. But the problem becomes more pronounced when you do things like route through a server that’s located very far from you (if I use an Australian server, each request has to travel all the way to Australia and back each time), or when every millisecond matters to what you’re doing.

- **You use more bandwidth:** This matters more for those who use a small, limited mobile data plan, but it’s worth mentioning. Because of encryption and a lot of other stuff I don’t understand, using a VPN [slightly increases your data usage](https://www.tomsguide.com/features/how-much-data-does-a-vpn-really-use).

- **A false sense of security and anonymity:** Despite the advantages above, websites still get *plenty* of information about you depending on your [operating system](https://domford.net/posts/exorcising-operating-system/), [browser](https://domford.net/posts/exorcising-web-browser/), usage habits and preferences. Even with a VPN, you can still be identified much of the time through piecing together other data. So a potential downside is if you think that the VPN is protecting you more than it is, and perhaps become sloppy in other aspects of browsing hygiene.

# Two ways to use a VPN
Depending on your weighing of the upsides and downsides we’ve talked about here, there are two main options for using a VPN to consider (aside from just not using one at all, of course).

One is to set and forget. You turn it on and leave it on, and only turn it off or use split tunnelling when you run into specific issues. This gives you the best protection and privacy, but also exacerbates the downsides. What you will most notice on a daily basis is filling out more CAPTCHAs.

The other is to leave it off and turn it on for specific activities. Maybe that’s just Netflix, or it’s for services you don’t like or trust as much, like AI chatbots or social media or Amazon. Or maybe it’s for when you’re doing naughty things like pirating. This gives you the benefits of a VPN when you really need it without exposing yourself to the issues on a regular basis, but also runs the risk of you forgetting about the VPN when you do need it.

# Free and open-source?
With VPNs, we come to our first hurdle with FOSS (free, open-source software). The nature of a VPN and its requirements means that it is not feasible to offer it for free. *Don’t touch free VPNs with a bargepole.* They are the epitome of the adage, ‘if you’re not the customer, you’re the product’. At *best*, the free VPN exploits its position as your middleman to harvest all of your lovely, juicy data to sell on. But there are far worse potential downsides, including malware. Just don’t do it. 

What about open source? Some argue that open source means worse security. A potential attacker can see the VPN’s source code, and can therefore figure out a way to attack it. Open source goes against the idea of [security through obscurity](https://en.wikipedia.org/wiki/Security_through_obscurity). The problem with this is that users then have to *trust* the vendor, and if you’re looking into using a VPN, you probably already have trust issues when it comes to tech companies. Plus, attackers can more easily keep a *vulnerability* secret when they find it in non-open-source code, deploying it at the perfect moment. Instead, modern cybersecurity tends to prefer [Kerckhoff’s principle](https://en.wikipedia.org/wiki/Kerckhoffs's_principle), the idea that a cryptosystem should be secure, even if everything about it is known except for the key. 

So, for our VPN we’re looking for open source, but *not* free.

This post has already gotten too long and has been unfinished for too long, so I won’t do a comparison table here, I’ll just shout-out my choice: [Mullvad](https://mullvad.net/en).

Now, I’m not a dissident or a spy or anything like that, but if I were, I would trust Mullvad. They have a policy of not logging *any* customer data of any kind. Your account is simply a string of characters with no password. Bills are payable by convenient digital solutions like Google and Apple Pay, card, and PayPal, but they also accept cryptocurrency and even envelopes of cash if you want to be totally anonymous. [Their no-logging policy was proven in 2023](https://www.techradar.com/news/mullvads-no-log-policy-proven-after-police-raid) when the Swedish police tried to seize Mullvad’s computers at their Gothenburg office, but left empty handed because there simply was no customer data to seize.

Aside from that, their VPN is fully-featured – with DNS blockers, split-tunnelling, quantum-resistant tunnels and more sci-fi-sounding things – and has plenty of high-quality connections around the world. They also have a fair, transparent pricing scheme: €5 per month. The price is the same no matter how long one signs up for, and hasn’t changed since 2009. There are no sales, ever. It’s a refreshing approach that makes it feel like a fair and transparent price, and not like leaving the F part of FOSS means being swallowed back in by all of the big tech, [battlepass-capitalism](https://doi.org/10.1177/1469540521993930) bullshit.

Using a VPN is maybe overkill for many people, and using Mullvad also feels a little overkill. But, for the price, it feels good to have an extra layer of protection from datafication and ads, and to know that my using Mullvad is just a little bit irritating to the tech bros.
