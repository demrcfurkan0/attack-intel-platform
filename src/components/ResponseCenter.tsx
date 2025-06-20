import React, { useState, useRef, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import ReactMarkdown from 'react-markdown';

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Textarea } from "@/components/ui/textarea";
import { Input } from "@/components/ui/input";
import { Checkbox } from "@/components/ui/checkbox";
import { Label } from "@/components/ui/label";
import { Separator } from "@/components/ui/separator";
import { ScrollArea } from '@/components/ui/scroll-area';
import { Loader2, AlertCircle, ShieldCheck, History, Clock, Tag, FileText, X, ListTodo, Bot, Send } from 'lucide-react';

import { useToast } from '@/hooks/use-toast';
import { getPredictionLogById, updatePredictionStatus, updatePredictionTags } from '@/services/reportService';
import { blockIpAddress, getIncidentHistory, executeAction } from '@/services/responseService';
import { postChatQuery } from '@/services/chatbotService';
import { PredictionLog, ResponseHistory } from '@/types/apiTypes';

type PlaybookTask = { id: string; label: string; actionId?: 'block_ip' | 'isolate_app'; };
type Playbook = { [attackType: string]: PlaybookTask[]; };
const PLAYBOOKS: Playbook = {
  'SQL_Injection': [ { id: 'sqli_review_ip', label: 'Review Source IP and Geolocation' }, { id: 'sqli_validate_url', label: 'Validate Vulnerable URL and Parameter' }, { id: 'sqli_isolate_app', label: 'Isolate Web Application', actionId: 'isolate_app' }, { id: 'sqli_notify_dev', label: 'Notify Development Team' }, ],
  'DoS/DDoS': [ { id: 'ddos_analyze_traffic', label: 'Analyze Traffic Pattern' }, { id: 'ddos_block_ip', label: 'Block Source IP', actionId: 'block_ip' }, { id: 'ddos_scale_resources', label: 'Scale Up Resources (Simulated)' }, { id: 'ddos_enable_cdn', label: 'Enable CDN Protection (Simulated)' }, ],
  'BruteForce': [ { id: 'bf_check_account', label: 'Check for Successful Login' }, { id: 'bf_lock_account', label: 'Lock Targeted Account(s) (Simulated)' }, { id: 'bf_block_ip', label: 'Block Source IP', actionId: 'block_ip' }, { id: 'bf_enforce_mfa', label: 'Enforce MFA for User' }, ],
  'default': [ { id: 'def_triage', label: 'Perform Initial Triage' }, { id: 'def_gather_evidence', label: 'Gather Additional Evidence' }, ]
};
const extractIpFromSource = (sourceInfo: string): string | null => {
    const ipRegex = /(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/;
    const match = sourceInfo.match(ipRegex);
    return match ? match[0] : null;
};

type Message = { sender: 'user' | 'bot'; text: string; };
interface ChatbotProps { incident: PredictionLog; }
const Chatbot: React.FC<ChatbotProps> = ({ incident }) => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const scrollAreaRef = useRef<HTMLDivElement>(null);

  const chatMutation = useMutation({
    mutationFn: (prompt: string) => postChatQuery({ prompt, incident_details: incident }),
    onSuccess: (data) => setMessages(prev => [...prev, { sender: 'bot', text: data.data.response }]),
    onError: () => setMessages(prev => [...prev, { sender: 'bot', text: "Sorry, I couldn't get a response. Please try again." }])
  });

  const handleSend = () => {
    if (!input.trim()) return;
    setMessages(prev => [...prev, { sender: 'user', text: input }]);
    chatMutation.mutate(input);
    setInput('');
  };

  useEffect(() => {
    if (scrollAreaRef.current) {
        scrollAreaRef.current.scrollTo({ top: scrollAreaRef.current.scrollHeight, behavior: 'smooth' });
    }
  }, [messages]);

  return (
    <Card className="glass-morphism h-[500px] flex flex-col">
      <CardHeader><CardTitle className="flex items-center"><Bot className="w-5 h-5 mr-2" /> CyberShield Co-Pilot</CardTitle></CardHeader>
      <CardContent className="flex-grow flex flex-col p-0">
        <ScrollArea className="flex-grow p-4" ref={scrollAreaRef}>
            <div className="space-y-4">
            {messages.map((msg, index) => (
                <div key={index} className={`flex items-start gap-3 ${msg.sender === 'user' ? 'justify-end' : ''}`}>
                    {msg.sender === 'bot' && <div className="p-2 bg-cyber-primary rounded-full text-cyber-dark flex-shrink-0"><Bot size={16}/></div>}
                    <div className={`p-3 rounded-lg max-w-xs md:max-w-md ${msg.sender === 'bot' ? 'bg-cyber-darker' : 'bg-cyber-secondary'}`}>
                        <div className="prose prose-sm prose-invert break-words">
                          <ReactMarkdown>{msg.text}</ReactMarkdown>
                        </div>
                    </div>
                </div>
            ))}
            {chatMutation.isPending && ( <div className="flex items-start gap-3"><div className="p-2 bg-cyber-primary rounded-full text-cyber-dark flex-shrink-0"><Loader2 size={16} className="animate-spin"/></div><div className="p-3 rounded-lg bg-cyber-darker">Thinking...</div></div> )}
            </div>
        </ScrollArea>
        <div className="p-4 border-t border-cyber-light/20 flex items-center gap-2">
            <Input placeholder="Ask about this incident..." value={input} onChange={e => setInput(e.target.value)} onKeyDown={e => e.key === 'Enter' && !e.shiftKey && (e.preventDefault(), handleSend())} disabled={chatMutation.isPending} />
            <Button onClick={handleSend} disabled={chatMutation.isPending} size="icon"><Send size={16}/></Button>
        </div>
      </CardContent>
    </Card>
  );
};

  

const ResponseCenter = () => {
    const { predictionId } = useParams<{ predictionId: string }>();
    const queryClient = useQueryClient();
    const { toast } = useToast();
    const [note, setNote] = useState('');
    const [currentTag, setCurrentTag] = useState('');

    const { data: alert, isLoading: isLoadingAlert, isError: isErrorAlert } = useQuery({ queryKey: ['predictionLog', predictionId], queryFn: () => getPredictionLogById(predictionId!).then(res => res.data), enabled: !!predictionId });
    const { data: incidentHistory, isLoading: isLoadingHistory } = useQuery({ queryKey: ['incidentHistory', predictionId], queryFn: () => getIncidentHistory(predictionId!).then(res => res.data), enabled: !!predictionId });
    
    const logActionMutation = useMutation({ mutationFn: (actionTitle: string) => executeAction({ action_title: actionTitle, target_prediction_id: predictionId! }), onSuccess: () => { queryClient.invalidateQueries({ queryKey: ['incidentHistory', predictionId] }); }, onError: (error: any) => toast({ variant: "destructive", title: "Logging Failed", description: error.response?.data?.detail }) });
    const blockIpMutation = useMutation({ mutationFn: (ip: string) => Promise.all([blockIpAddress(ip), logActionMutation.mutateAsync(`Playbook ACTION executed: "Block Source IP"`)]), onSuccess: ([blockData]) => { toast({ title: "Action Successful", description: (blockData as any).data.message }); }, onError: (error: any) => toast({ variant: "destructive", title: "Action Failed", description: error.response?.data?.detail }) });
    const updateStatusMutation = useMutation({ mutationFn: (status: string) => Promise.all([updatePredictionStatus(predictionId!, status), logActionMutation.mutateAsync(`Status changed to: ${status}`)]), onSuccess: ([statusUpdateData]) => { toast({ title: "Status Updated", description: (statusUpdateData as any).data.message }); queryClient.invalidateQueries({ queryKey: ['predictionLog', predictionId] }); }, onError: (error: any) => toast({ variant: "destructive", title: "Status Update Failed", description: error.response?.data?.detail }) });
    const updateTagsMutation = useMutation({ mutationFn: (newTags: string[]) => updatePredictionTags(predictionId!, newTags), onSuccess: () => { toast({ title: "Tags Updated" }); queryClient.invalidateQueries({ queryKey: ['predictionLog', predictionId] }); }, onError: (error: any) => toast({ variant: "destructive", title: "Tag Update Failed", description: error.response?.data?.detail }) });

    const handleBlockIp = () => { if (!alert) return; const ip = extractIpFromSource(alert.source_of_data); if (ip) blockIpMutation.mutate(ip); else toast({ variant: "destructive", title: "Cannot Block", description: "No valid IP address found in source." }); };
    const handleGenericAction = (task: PlaybookTask) => { logActionMutation.mutate(`Playbook ACTION executed: "${task.label}"`); };
    const handleAddNote = () => { if (!note.trim()) return; logActionMutation.mutate(`Note added: "${note.trim()}"`); setNote(''); };
    const handleAddTag = (e: React.KeyboardEvent<HTMLInputElement>) => { if (e.key === 'Enter' && currentTag.trim()) { e.preventDefault(); const existingTags = alert?.tags || []; const newTag = currentTag.trim().toLowerCase(); if (!existingTags.includes(newTag)) updateTagsMutation.mutate([...existingTags, newTag]); setCurrentTag(''); } };
    const handleRemoveTag = (tagToRemove: string) => { if (!alert?.tags) return; updateTagsMutation.mutate(alert.tags.filter(tag => tag !== tagToRemove)); };
    const handleTaskCompletion = (taskLabel: string, isCompleted: boolean) => { const actionTitle = `Playbook step ${isCompleted ? 'COMPLETED' : 'REVERTED'}: "${taskLabel}"`; logActionMutation.mutate(actionTitle); };

    if (!predictionId) { return ( <Card className="glass-morphism h-96 flex flex-col items-center justify-center"><CardHeader><CardTitle>Incident Response Center</CardTitle></CardHeader><CardContent className="text-center"><ShieldCheck className="w-16 h-16 mx-auto text-cyber-primary mb-4" /><p className="text-gray-400">Select an alert from the "Alerts" tab to begin analysis and response.</p></CardContent></Card> ); }
    if (isLoadingAlert) return <div className="flex justify-center items-center h-96"><Loader2 className="w-12 h-12 animate-spin text-cyber-primary" /></div>;
    if (isErrorAlert || !alert) return <div className="text-cyber-accent text-center p-10"><AlertCircle className="w-12 h-12 mx-auto mb-4" />Failed to load incident details.</div>;

    const alertStatus = alert.status || 'new';
    const attackType = alert.prediction_result.prediction_label;
    const playbookTasks = PLAYBOOKS[attackType] || PLAYBOOKS['default'];
    const completedTaskLabels = new Set(incidentHistory?.filter(h => h.action_title.startsWith('Playbook step COMPLETED:')).map(h => h.action_title.replace('Playbook step COMPLETED: "', '').replace('"', '')) || []);
    const executedActionLabels = new Set(incidentHistory?.filter(h => h.action_title.startsWith('Playbook ACTION executed:')).map(h => h.action_title.replace('Playbook ACTION executed: "', '').replace('"', '')) || []);
    const checklistTasks = playbookTasks.filter(task => !task.actionId);
    const actionTasks = playbookTasks.filter(task => task.actionId);
    const specialActions: { [key: string]: { handler: () => void; mutation: any; } } = { 'block_ip': { handler: handleBlockIp, mutation: blockIpMutation }, 'isolate_app': { handler: () => handleGenericAction({id: 'sqli_isolate_app', label: 'Isolate Web Application'}), mutation: logActionMutation }, };

    return (
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <div className="lg:col-span-2 space-y-6">
                <Card className="glass-morphism">
                    <CardHeader>
                        <div className="flex justify-between items-start">
                            <div>
                                <CardTitle>Incident Details: {alert.prediction_result.prediction_label}</CardTitle>
                                <CardDescription>ID: {alert._id}</CardDescription>
                            </div>
                            <Badge variant={alertStatus === 'resolved' ? 'default' : alertStatus === 'triaged' ? 'secondary' : 'destructive'} className="capitalize">{alertStatus}</Badge>
                        </div>
                    </CardHeader>
                    <CardContent>
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
                            <div><strong>Source:</strong> <span className="font-mono text-cyber-warning break-all">{alert.source_of_data}</span></div>
                            <div><strong>Detected At:</strong> <span className="font-mono">{new Date(alert.created_at).toLocaleString()}</span></div>
                            <div><strong>Model Confidence:</strong> <span className="font-mono text-cyber-primary">{alert.prediction_result.probabilities ? `${(Math.max(...alert.prediction_result.probabilities) * 100).toFixed(2)}%` : 'N/A'}</span></div>
                            <div><strong>Simulation ID:</strong> <span className="font-mono break-all">{alert.simulation_id || 'N/A'}</span></div>
                        </div>
                        <div className="mt-4 pt-4 border-t border-cyber-light/20">
                           <h4 className="text-sm font-medium text-gray-300 mb-2 flex items-center"><Tag className="w-4 h-4 mr-2"/>Tags</h4>
                           <div className="flex flex-wrap items-center gap-2">
                               {alert.tags?.map(tag => <Badge key={tag} variant="secondary" className="capitalize">{tag} <X className="ml-1.5 h-3 w-3 cursor-pointer hover:text-red-400" onClick={() => handleRemoveTag(tag)}/> </Badge>)}
                               <Input className="h-7 w-28 bg-transparent text-xs flex-grow" placeholder="+ Add Tag & Enter" value={currentTag} onChange={(e) => setCurrentTag(e.target.value)} onKeyDown={handleAddTag} disabled={updateTagsMutation.isPending}/>
                           </div>
                        </div>
                    </CardContent>
                </Card>
                <Card className="glass-morphism"><CardHeader><CardTitle className="flex items-center"><FileText className="w-5 h-5 mr-2"/>Analyst Notes</CardTitle></CardHeader><CardContent className="space-y-4"><Textarea placeholder="Add your investigation notes here..." value={note} onChange={(e) => setNote(e.target.value)} className="bg-cyber-darker/50 border-cyber-light/30" /><Button onClick={handleAddNote} disabled={logActionMutation.isPending || !note.trim()}>{logActionMutation.isPending && <Loader2 className="w-4 h-4 mr-2 animate-spin"/>} Add Note</Button></CardContent></Card>
                <Card className="glass-morphism"><CardHeader><CardTitle className="flex items-center"><History className="w-5 h-5 mr-2" />Action History for this Incident</CardTitle></CardHeader><CardContent>{isLoadingHistory ? <div className="flex justify-center p-4"><Loader2 className="animate-spin" /></div> : !incidentHistory || incidentHistory.length === 0 ? <p className="text-gray-400 text-sm">No actions or notes recorded yet.</p> : <div className="space-y-4">{incidentHistory.map((h) => (<div key={h.id} className="flex items-start space-x-3 text-sm"><Clock className="w-4 h-4 mt-0.5 text-gray-500 flex-shrink-0"/><div>{h.action_title.startsWith('Note added:') ? <p className="text-gray-200 italic">{h.action_title.replace('Note added: ', '')}</p> : <p className="text-gray-200 font-medium">{h.action_title}</p>}<p className="text-xs text-gray-400">by {h.executed_by} at {new Date(h.timestamp).toLocaleString()}</p></div></div>))}</div>}</CardContent></Card>
            </div>
            <div className="lg:col-span-1 space-y-6">
                <Card className="glass-morphism">
                    <CardHeader>
                        <CardTitle className="flex items-center">
                            <ListTodo className="w-5 h-5 mr-2"/>Incident Playbook
                        </CardTitle>
                        <CardDescription>Follow these steps to resolve the incident.</CardDescription>
                    </CardHeader>
                    <CardContent className="flex flex-col space-y-4">
                        <div className="space-y-3">
                            {checklistTasks.map((task) => {
                                const isCompleted = completedTaskLabels.has(task.label);
                                return (
                                    <div key={task.id} className="flex items-center space-x-3">
                                        <Checkbox id={task.id} checked={isCompleted} onCheckedChange={(checked) => handleTaskCompletion(task.label, Boolean(checked))}/>
                                        <Label htmlFor={task.id} className={`text-sm ${isCompleted ? 'line-through text-gray-500' : 'text-gray-200'}`}>{task.label}</Label>
                                    </div>
                                );
                            })}
                        </div>
                        {actionTasks.length > 0 && <Separator className="bg-cyber-light/20"/>}
                        <div className="space-y-2">
                            {actionTasks.map(task => {
                                const actionConfig = task.actionId ? specialActions[task.actionId] : null;
                                const isActionExecuted = executedActionLabels.has(task.label);
                                if (!actionConfig) return null;
                                return (
                                    <Button key={task.id} className="w-full justify-start" variant="destructive" onClick={actionConfig.handler} disabled={isActionExecuted || actionConfig.mutation.isPending}>
                                        {actionConfig.mutation.isPending ? <Loader2 className="w-4 h-4 mr-2 animate-spin" /> : <ShieldCheck className="w-4 h-4 mr-2" />}
                                        {task.label}
                                    </Button>
                                );
                            })}
                        </div>
                        <Separator className="bg-cyber-light/20"/>
                        <div className="space-y-2">
                            {(alertStatus !== 'triaged' && alertStatus !== 'resolved') && (
                                <Button className="w-full" variant="outline" onClick={() => updateStatusMutation.mutate('triaged')} disabled={updateStatusMutation.isPending}>
                                    Acknowledge & Triage
                                </Button>
                            )}
                            {alertStatus !== 'resolved' && (
                                <Button className="w-full" variant="outline" onClick={() => updateStatusMutation.mutate('resolved')} disabled={updateStatusMutation.isPending}>
                                    Mark as Resolved
                                </Button>
                            )}
                        </div>
                        {alertStatus === 'resolved' && (
                            <p className="text-sm text-green-400 text-center pt-2">This incident has been resolved.</p>
                        )}
                    </CardContent>
                </Card>
                <Chatbot incident={alert} />
            </div>
        </div>
    );
};

export default ResponseCenter;