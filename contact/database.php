$hostname = '{https://mail.google.com/mail/u/0/?fbclid=IwAR1pYSsBCX7DTi7cepg-xY1RQTr5hDZtOGDfGkrIot5EugAOSX2eELw597Q#inbox:993/imap/ssl}INBOX';
$username = ' root@localhost';
$password = ' ';
$inbox = imap_open(https://mail.google.com/mail/u/0/?fbclid=IwAR1pYSsBCX7DTi7cepg-xY1RQTr5hDZtOGDfGkrIot5EugAOSX2eELw597Q#inbox,$root@localhost,$password);
$emails = imap_search($inbox,'ALL');
foreach($emails as $e){
    $overview = imap_fetch_overview($https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox,$e,0);
    $Subject = imap_fetchbody($https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox,$e,2);
    // the body of the message is in $Subject
    $details = $overview[0];
    
}
$cfg['Console']['Mode'] = 'show';

