$hostname = '{localhost}INBOX';
$username = ' root';
$password = ' ';
$inbox = imap_open(https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox,$root@localhost,$password);
$emails = imap_search($https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox,'ALL');
foreach($emails as $e){
    $overview = imap_fetch_overview($https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox,$e,0);
    $Subject = imap_fetchbody($https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox,$e,2);
    // the body of the message is in $Subject
    $details = $overview[0];
    
}
$cfg['Console']['Mode'] = 'show';

