$(Document).ready(function() {
    var nowQouteNum;
    var getRndQoute = function() {
      var i = Math.floor(Math.random() * (qoutes.length - 1 - 0 + 1)) + 0;
  
      while (i === nowQouteNum) {
        i = Math.floor(Math.random() * (qoutes.length - 1 - 0 + 1)) + 0;
      };
      
      $("#text").text(qoutes[i].qText);
      $("#autor").text(qoutes[i].qAutor);
      nowQouteNum = i;
      };
    
    $('#getQoute').click(function() {
      getRndQoute()
      console.log('itsworking');
    }); 
    
    getRndQoute();
  });
  
  
  var qoutes = [{
    qText: "Is it that we collectively thought Steve Jobs was a great man, even when we knew he made billions off the backs of children? Or maybe it's that it feels like all our heroes are counterfeit? The world itself just one big hoax, spamming each other with our burning commentary bullshit, masquerading this insight; our social media faking this intimacy. Or is it that we voted for this? Not with our rigged elections, but with our things, our property, our money. I'm not saying anything new, we all know why we do this, not because Hunger Games books makes us happy, but because we want to be sedated. Because it's painful not to pretend, because we're cowards. Fuck society.",
    qAutor: "Elliot"
  }, {
    qText: "The world is a dangerous place, Elliott, not because of those who do evil, but because of those who look on and do nothing.",
    qAutor: "Mr. Robot"
  }, {
    qText: "I never want to be right about my hacks, but people always find a way to disappoint.",
    qAutor: "Elliot"
  }, {
    qText: "Hello friend. Hello friend? That's lame. Maybe I should give you a name. But that's a slippery slope, you're only in my head, we have to remember that. Shit, this actually happened, I'm talking to an imaginary person. What I'm about to tell you is top secret. A conspiracy bigger than all of us. There's a powerful group of people out there that are secretly running the world. I'm talking about the guys no one knows about, the ones that are invisible. The top 1% of the top 1%, the guys that play God without permission. And now I think they're following me.",
    qAutor: "Elliot"
  }, {
    qText: "A bug is never just a mistake. It represents something bigger. An error of thinking that makes you who you are.",
    qAutor: "Elliot"
  }, {
    qText: "We're all living in each other's paranoia.",
    qAutor: "Elliot"
  }, {
    qText: "Power belongs to those who take it.",
    qAutor: "Tyrell Wellick"
  }, {
    qText: "I wanted to save the world.",
    qAutor: "Elliot"
  }, {
    qText: "Though she's a psychologist she's really bad at reading people but I'm good at reading people. My secret? I look for the worst in them.",
    qAutor: "Elliot"
  }, {
    qText: "The concept of waiting bewilders me. There are always deadlines. There are always ticking clocks.",
    qAutor: "Whiterose"
  }, {
    qText: "People walk around, act like they know what hate means. Nah, no one does, until you hate yourself. I mean truly hate yourself. That's power.",
    qAutor: "Fernando Vera"
  }, {
    qText: "Even extraordinary people, and I believe you are, are driven by human banalities.",
    qAutor: "Tyrell Wellick"
  }, {
    qText: "If you want to change things, perhaps you should try from within, because this is what happens from the outside.",
    qAutor: "Terry Colby"
  }, {
    qText: "No rest for the wicked.",
    qAutor: "Mr. Robot"
  }, {
    qText: "People are all just people, right? When it gets down to it, everyone's the same. They love something. They want something. They fear something. Specifics help, but specifics don't change the way that everyone is vulnerable. It just changes the way that we access those vulnerabilities.",
    qAutor: "Mobley"
  }, {
    qText: "Two days ago I strangled a woman to death just with my hands. That's a strange sensation. Something so tremendous done by something so simple. The first ten seconds were uncomfortable, a feeling of limbo, but then your muscles tense, and she struggles and fights, but it almost disappears in the background along with everything else in the world. At that moment it's just you and absolute power, nothing else. That moment stayed with me. I thought I'd feel guilty for being a murderer, but I don't. I feel wonder.",
    qAutor: "Tyrell Wellick"
  }, {
    qText: "There's a smart time to be scared, bro... and a stupid time.",
    qAutor: "Fernando Vera"
  }, {
    qText: "You hack people. I hack time.",
    qAutor: "Whiterose"
  }, {
    qText: "You're never sure about anything unless there's something to be sure about.",
    qAutor: "Gideon Goddard"
  }, {
    qText: "Who do you think I am?",
    qAutor: "Darlene"
  }];
  