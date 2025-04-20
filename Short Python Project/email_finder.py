import re
# It Finds All Emails Form A Given Text

str='''
           Petrova (October 26, 2019). "Gmail dominates consumer email with 1.5 billion users". CNBC.com. Archived from the original on November 17, 2019. Retrieved November 19, 2019.
 Siegler, MG (March 14, 2010). "The Key To Gmail: Sh*t Umbrellas". TechCrunch. AOL. Archived from the original on October 22, 2016. Retrieved October 27, 2018.
 "Manage files in your Google Drive storage - Gmail Help". support.google.com. Retrieved February 11, 2023.
 "Buy more Google storage - Computer - Google Drive Help". support.google.com. Retrieved April 4, 2023.
 "Group emails into conversations - Computer - Gmail Help". support.google.com. Retrieved December 8, 2023.
 Bergen, Mark (June 23, 2017). "Google Will Stop Reading Your Emails for Gmail Ads". Bloomberg.com. Bloomberg L.P. Archived from the original on June 23, 2017. Retrieved October 27, 2018.(subscription required)
 Singer, Michael (March 31, 2004). "Google Testing Free Webmail". Internet News. Archived from the original on December 23, 2016. Retrieved October 27, 2018.
 Kuchinskas, Susan (April 1, 2005). "Endless Gmail Storage". Internet News. Archived from the original on April 28, 2016. Retrieved October 27, 2018.
 Moltzen, Edward F. (October 21, 2007). "Google Ups GMail to 4 GB of Storage". CRN. Retrieved October 27, 2022.
 Behrens, Nicholas (April 24, 2012). "Gmail, now with 10 GB of storage (and counting)". Official Gmail Blog. Archived from the original on October 31, 2016. Retrieved October 27, 2018.
 Bavor, Clay (May 13, 2013). "Bringing it all together: 15 GB now shared between Drive, Gmail, and Google+ Photos". Google Drive Blog. Archived from the original on December 30, 2017. Retrieved October 27, 2018.
 Petkov, Jason (May 13, 2013). "15GB of Free Storage, Thanks Google!". W3Reports. Archived from the original on October 27, 2018. Retrieved October 27, 2018.
 "Pricing guide". Archived from the original on September 16, 2018. Retrieved October 27, 2018.
 "Send attachments with your Gmail message". Gmail Help. Archived from the original on September 16, 2016. Retrieved October 27, 2018.
 "Receive emails of up to 50 MB in Gmail". G Suite Updates. March 1, 2017. Archived from the original on March 2, 2017. Retrieved October 27, 2018.
 Coldewey, Devin (March 1, 2017). "Huzzah! Gmail now accepts attachments up to 50 MB". TechCrunch. AOL. Archived from the original on March 2, 2017. Retrieved October 27, 2018.
 "Send Google Drive attachments in Gmail". Gmail Help. Archived from the original on December 31, 2018. Retrieved October 27, 2018.
 Lenssen, Philipp (June 2, 2008). "Kevin Fox of Gmail & FriendFeed on User Experience Design". Google Blogoscoped. Archived from the original on September 6, 2013. Retrieved October 27, 2018.
 Cornwell, Jason (November 1, 2011). "Gmail's new look". Official Gmail Blog. Archived from the original on November 26, 2016. Retrieved October 27, 2018.
 Houston, Thomas (November 1, 2011). "Gmail redesign adds enhanced search box, profile pictures, conversations, and more". The Verge. Vox Media. Archived from the original on November 26, 2016. Retrieved October 27, 2018.
 "Gmail New Look will be released to all users starting March 27th". G Suite Updates. March 20, 2012. Archived from the original on November 26, 2016. Retrieved October 27, 2018.
 Gilad, Itamar (May 29, 2013). "A new inbox that puts you back in control". Official Gmail Blog. Archived from the original on November 26, 2016. Retrieved October 27, 2018.
 Bonnington, Christina (May 29, 2013). "Gmail's New Inbox Sorts Emails Into Tabbed Categories". Wired. Archived from the original on November 26, 2016. Retrieved October 27, 2018.
 Savov, Vlad (April 25, 2018). "Gmail's biggest redesign is now live". The Verge. Vox Media. Archived from the original on April 25, 2018. Retrieved October 27, 2018.
 "Google will soon let you opt out of Gmail's data-hungry smart features entirely". The Verge. November 16, 2020. Retrieved November 16, 2020.
 "Google begins rolling out Chat and Rooms tabs in Gmail for all accounts". Android Central. April 5, 2021. Retrieved April 6, 2021.
 "Google made chats in Gmail available to all users of the service". Gizchina.com. April 5, 2021. Retrieved April 6, 2021.
 Mehta, Ivan (July 28, 2022). "Gmail rolls out its latest Material You redesign and search improvements to all users". TechCrunch. Retrieved August 4, 2022.
 "Mark or unmark Spam in Gmail". Gmail Help. Archived from the original on August 15, 2018. Retrieved October 27, 2018.
 Coleman, Keith (June 5, 2008). "Introducing Gmail Labs". Official Gmail Blog. Archived from the original on November 26, 2016. Retrieved October 27, 2018.
 Williams, Owen (June 23, 2015). "Gmail's 'Undo Send' feature finally graduates out of labs after six years". The Next Web. Archived from the original on September 25, 2018. Retrieved October 27, 2018.
 "About Google Labs". Archived from the original on May 1, 2016. Retrieved October 27, 2018.
 Moolenaar, Bram (October 15, 2012). "Find your stuff faster in Gmail and Search". Official Gmail Blog. Archived from the original on July 10, 2016. Retrieved October 27, 2018.
 Racz, Balazs (May 23, 2013). "Search emails, Google Drive, Calendar and more as you type". Official Gmail Blog. Archived from the original on November 26, 2016. Retrieved October 27, 2018.
 Protalinski, Emil (May 23, 2013). "Google adds Google Drive files and Calendar events to Gmail's search for US users". The Next Web. Archived from the original on September 6, 2018. Retrieved October 27, 2018.
 "Gmail workarounds for sub-string (partial word) search". Confluence. Archived from the original on January 17, 2017. Retrieved October 27, 2018.
 "Change your Gmail language settings". Gmail Help. Archived from the original on May 27, 2018. Retrieved October 27, 2018.
 Warren, C. Andrew (October 9, 2012). "Communicate more easily across languages in Gmail". The Keyword. Archived from the original on October 27, 2018. Retrieved October 27, 2018.
 Lardinois, Frederic (October 9, 2012). "Google Brings More Than 100 Virtual Keyboards, Transliterations And IMEs To Gmail". TechCrunch. AOL. Archived from the original on November 26, 2016. Retrieved October 27, 2018.
 Xiao, Xiangye (October 22, 2013). "Handwriting input comes to Gmail and Google Docs". Official Gmail Blog. Archived from the original on February 9, 2017. Retrieved October 27, 2018.
 Monferrer, Pedro Chaparro (August 5, 2014). "A first step toward more global email". Official Gmail Blog. Archived from the original on November 26, 2016. Retrieved October 27, 2018.
 Grandoni, Dino (August 5, 2014). "Google To Recognize Emails That Use Special Characters". Huffington Post. Archived from the original on January 8, 2017. Retrieved October 27, 2018.
 Panchapakesan, Venkat (June 1, 2011). "Our plans to support modern browsers across Google Apps". Official Gmail Blog. Archived from the original on October 2, 2016. Retrieved October 27, 2018.
 "Supported browsers". Chat Help. Archived from the original on March 19, 2017. Retrieved October 27, 2018.
 "Supported browsers". Gmail Help. Retrieved September 24, 2023.
 "Use the latest version of Gmail in your browser". Gmail Help. Retrieved September 24, 2023.
 Boursetty, Benoît (August 31, 2011). "Using Gmail, Calendar and Docs without an Internet connection". Official Gmail Blog. Archived from the original on November 14, 2016. Retrieved October 27, 2018.
 Zukerman, Erez (May 10, 2013). "Review: Give Gmail an extreme makeover with Gmail Offline". PC World. International Data Group. Archived from the original on May 7, 2017. Retrieved October 27, 2018.
 Siegler, MG (May 11, 2011). "Coming This Summer: Fully Offline Gmail, Google Calendar, And Google Docs". TechCrunch. AOL. Archived from the original on November 26, 2016. Retrieved October 27, 2018.
 Kroeger, Rob (April 7, 2009). "A new mobile Gmail experience for iPhone and Android". Official Gmail Blog. Archived from the original on November 26, 2016. Retrieved October 27, 2018.
 "Gmail - Email by Google on the iOS App Store". iTunes. Apple. Archived from the original on November 26, 2016. Retrieved October 27, 2018.
 "Gmail on the Google Play Store". Google Play. Archived from the original on November 25, 2016. Retrieved October 27, 2018.
 Izatt, Matthew (November 3, 2014). "A more modern Gmail app for Android". Official Gmail Blog. Archived from the original on November 26, 2016. Retrieved October 27, 2018.
 Izatt, Matthew (November 7, 2016). "Gmail and Google Calendar get a whole lot better on iOS". The Keyword Google Blog. Archived from the original on November 19, 2016. Retrieved October 27, 2018.
 Welch, Chris (November 7, 2016). "Google just redesigned Gmail for iPhone and made it way faster". The Verge. Vox Media. Archived from the original on November 26, 2016. Retrieved October 27, 2018.
 Lawler, Richard (May 4, 2017). "Now the Android Gmail app keeps an eye out for phishing links". Engadget. AOL. Archived from the original on May 4, 2017. Retrieved October 27, 2018.
 Tung, Liam (May 4, 2017). "Google gives Android Gmail users new shady link warnings amid fake Docs attack". ZDNet. CBS Interactive. Archived from the original on March 27, 2019. Retrieved October 27, 2018.
 Perez, Sarah (May 4, 2017). "Google adds phishing protection to Gmail on Android". TechCrunch. AOL. Archived from the original on May 4, 2017. Retrieved October 27, 2018.
 Vincent, James (May 17, 2017). "Smart Reply is coming to Gmail for Android and iOS". The Verge. Vox Media. Archived from the original on May 17, 2017. Retrieved October 27, 2018.
 Ingraham, Nathan (May 17, 2017). "Google's impersonal-but-handy Smart Replies come to the Gmail app". Engadget. AOL. Archived from the original on May 17, 2017. Retrieved October 27, 2018.
 "Inbox by Gmail on the iOS App Store". iTunes. Apple. Archived from the original on November 26, 2016. Retrieved October 27, 2018.
 "Inbox by Gmail on the Google Play Store". Google Play. Archived from the original on December 12, 2016. Retrieved October 27, 2018.
 "Read Gmail messages on other email clients using POP". Gmail Support. Archived from the original on November 26, 2016. Retrieved October 27, 2018.
 Mix (October 10, 2019). "Google is rolling out dark mode for Gmail and Maps". The Next Web. Archived from the original on October 10, 2019. Retrieved October 10, 2019.
 Pichai, Sundar (October 22, 2014). "An inbox that works for you". Official Gmail Blog. Archived from the original on October 24, 2016. Retrieved October 27, 2018.
 Bohn, Dieter (October 22, 2014). "Inbox is a total reinvention of email from Google". The Verge. Vox Media. Archived from the original on September 5, 2016. Retrieved October 27, 2018.
 Etherington, Darrell (October 22, 2014). "Google's Inbox is A New Email App From The Gmail Team Designed Not To Be Gmail". TechCrunch. AOL. Archived from the original on February 9, 2017. Retrieved October 27, 2018.
 Gawley, Alex (May 28, 2015). "Thanks to you, Inbox by Gmail is now open to everyone". Official Gmail Blog. Archived from the original on January 6, 2017. Retrieved October 27, 2018.
 Izatt, Matthew (September 12, 2018). "Inbox is signing off. Find your favorite features in the new Gmail". The Keyword. Archived from the original on September 12, 2018. Retrieved September 12, 2018.
 Schoon, Ben (March 19, 2019). "Inbox by Gmail officially shuts down on April 2nd, 2019". 9to5Google. Archived from the original on March 20, 2019. Retrieved April 3, 2019.
 Calore, Michael (August 25, 2010). "Gmail Gets Dialed Up a Notch With New Calling Feature". Wired. Archived from the original on December 22, 2016. Retrieved October 27, 2018.
 Nowak, Peter (August 25, 2010). "Google launches free voice calls from Gmail". CBC News. Archived from the original on February 9, 2017. Retrieved October 27, 2018.
 Mullany, Anjali (August 27, 2010). "Google announces via Twitter: 1,000,000 Gmail calls in 24 Hours". New York Daily News. Mortimer Zuckerman. Archived from the original on October 27, 2018. Retrieved October 27, 2018.
 Shankland, Stephen (August 26, 2010). "Google: 1 million Gmail calls on first day". CNN. Archived from the original on January 2, 2016. Retrieved October 27, 2018.
 Weintraub, Seth (March 18, 2014). "Google plans to kill Google Voice in coming months, integrate features into Hangouts". 9to5Google. Archived from the original on November 26, 2016. Retrieved October 27, 2018.
 Russell, Brandon (March 18, 2014). "Google Planning To Discontinue Google Voice In Favor of Hangouts". TechnoBuffalo. Archived from the original on November 5, 2018. Retrieved October 27, 2018.
 Guynn, Jessica (February 9, 2010). "Google aims to take on Facebook with new social feature called 'Buzz'". Los Angeles Times. Archived from the original on October 27, 2018. Retrieved October 27, 2018.
 Cheredar, Tom (July 11, 2011). "Google says Google+ integration for Gmail is coming; users sound off". VentureBeat. Archived from the original on November 26, 2016. Retrieved October 27, 2018.
 Horowitz, Bradley (October 14, 2011). "A fall sweep". Official Google Blog. Archived from the original on October 21, 2018. Retrieved October 27, 2018.
 Striebeck, Mark (December 8, 2011). "Gmail and Contacts get better with Google+". Official Gmail Blog. Archived from the original on February 9, 2017. Retrieved October 27, 2018.
 Horowitz, Bradley (July 27, 2015). "Everything in its right place". The Keyword. Archived from the original on April 12, 2019. Retrieved October 27, 2018.
 Green, Travis (May 15, 2013). "Send money to friends with Gmail and Google Wallet". Official Gmail Blog. Archived from the original on November 27, 2016. Retrieved October 27, 2018.
 Honig, Zach (May 15, 2013). "Google Wallet will soon let you send payments as a Gmail attachment". Engadget. AOL. Archived from the original on November 27, 2016. Retrieved October 27, 2018.
 "Send money or pay a request". Google Wallet Help. Retrieved October 27, 2018.
 Welch, Chris (March 14, 2017). "Gmail for Android now lets you send people money right in the app". The Verge. Vox Media. Archived from the original on March 14, 2017. Retrieved October 27, 2018.
 Lopez, Napier (March 14, 2017). "Google now lets you send money via Gmail on Android". The Next Web. Archived from the original on March 15, 2017. Retrieved October 27, 2018.
 Frank, Stefan (September 19, 2016). "See more, plan less – try Google Trips". The Keyword Google Blog. Archived from the original on December 6, 2016. Retrieved October 27, 2018.
 Newton, Casey (September 19, 2016). "Google Trips is a killer travel app for the modern tourist". The Verge. Vox Media. Archived from the original on November 30, 2016. Retrieved October 27, 2018.
 Perez, Sarah (April 26, 2017). "Personalized travel planner Google Trips gets better at handling your reservations". TechCrunch. AOL. Archived from the original on April 27, 2017. Retrieved October 27, 2018.
 Kastrenakes, Jacob (April 26, 2017). "Google's Trips app is becoming an even better travel companion". The Verge. Vox Media. Archived from the original on April 26, 2017. Retrieved October 27, 2018.
 Rideout, Ariel (July 24, 2008). "Making security easier". Official Gmail Blog. Archived from the original on November 26, 2016. Retrieved October 27, 2018.
 Kirk, Jeremy (January 2, 2007). "Google closes Gmail cross-site scripting vulnerability". InfoWorld. International Data Group. Archived from the original on October 27, 2018. Retrieved October 27, 2018.
 Schillace, Sam (January 12, 2010). "Default https access for Gmail". Official Gmail Blog. Archived from the original on November 26, 2016. Retrieved October 27, 2018.
 Grosse, Eric (June 5, 2012). "Security warnings for suspected state-sponsored attacks". Google Security Blog. Archived from the original on December 8, 2016. Retrieved October 27, 2018.
 "Google to warn users of 'state-sponsored attacks'". CBC News. June 6, 2012. Archived from the original on December 31, 2016. Retrieved October 27, 2018.
 Lidzborski, Nicolas (March 20, 2014). "Staying at the forefront of email security and reliability: HTTPS-only and 99.978% availability". Official Gmail Blog. Archived from the original on December 2, 2016. Retrieved October 27, 2018.
 "Check the security of your emails". Gmail Help. Archived from the original on November 26, 2016. Retrieved October 27, 2018.
 "File types blocked in Gmail". Gmail Help. Archived from the original on November 26, 2016. Retrieved October 27, 2018.
 Lardinois, Frederic (May 31, 2017). "Google says its machine learning tech now blocks 99.9% of Gmail spam and phishing messages". TechCrunch. AOL. Archived from the original on May 31, 2017. Retrieved October 27, 2018.
 Locklear, Mallory (May 31, 2017). "Google beefs up Gmail security to fight phishing attempts". Engadget. AOL. Archived from the original on May 31, 2017. Retrieved October 27, 2018.
 "Google Workspace security updates—November 2020". Google Cloud Blog. Retrieved September 14, 2022.
 "Email encryption in transit". Google Transparency Report. Archived from the original on October 31, 2018. Retrieved October 27, 2018.
 "Google 2-Step Verification". Archived from the original on November 25, 2016. Retrieved October 27, 2018.
 "Sign in with Google Prompts". Retrieved December 30, 2021.
 arnab112datta@gmail.com
 "Google 2-Step Verification". Archived from the original on December 4, 2016. Retrieved October 27, 2018.
 Shah, Nishit (October 21, 2014). "Strengthening 2-Step Verification with Security Key". Google Security Blog. Archived from the original on December 15, 2016. Retrieved October 27, 2018.
 Turner, Adam (November 5, 2014). "Google security keys may offer extra layer of online protection". The Sydney Morning Herald. Fairfax Media. Archived from the original on October 26, 2016. Retrieved October 27, 2018.
 "Can't sign in to your Google Account". Google Account Help. Archived from the original on October 7, 2018. Retrieved October 27, 2018.
 Perez, Sarah (August 6, 2014). "Why The Gmail Scan That Led To A Man's raju@gmail.in Arrest For Child Porn Was Not A Privacy Violation". TechCrunch. AOL. Archived from the original on March 23, 2017. Retrieved October 27, 2018.
 McCracken, Harry (April 1, 2014). "How Gmail Happened: The Inside Story of Its Launch 10 Years Ago". Time. Time Inc. Archived from the original on November 22, 2016. Retrieved October 27, 2018.
 "Google Gets the Message, Launches Gmail". Google News from Google. April 1, 2004. Archived from the original on November 10, 2018. Retrieved October 27, 2018.
 Oswald, Ed (November 2, 2006). "Google Offers Java-based Mobile Gmail". BetaNews. Archived from the original on November 5, 2018. Retrieved October 27, 2018.
 Pupius, Dan (October 29, 2007). "Code changes to prepare Gmail for the future". Official Gmail Blog. Archived from the original on November 26, 2016. Retrieved October 27, 2018.
 Jones, K.C. (October 24, 2007). "Gmail Now Has IMAP Support". InformationWeek. UBM Tech. Archived from the original on October 27, 2018. Retrieved October 27, 2018.

'''
email=re.findall(r"[a-zA-Z0-9._+%]+@[a-zA-Z0-9._+%]+[.][0-9a-zA-Z]+",str)
print(email)