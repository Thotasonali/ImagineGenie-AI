import { useEffect, useState } from 'react';
import { CreatorPanel } from './components/CreatorPanel';
import { Header } from './components/Header';
import { HistoryGrid } from './components/HistoryGrid';
import { PreviewPanel } from './components/PreviewPanel';
import { deleteHistoryItem, generateImage, getHistory } from './services/api';
import type { ImageRecord } from './types/image';
import './styles.css';

function App() {
  const [prompt, setPrompt] = useState('');
  const [style, setStyle] = useState('realistic');
  const [loading, setLoading] = useState(false);
  const [latestImage, setLatestImage] = useState<ImageRecord | null>(null);
  const [history, setHistory] = useState<ImageRecord[]>([]);

  async function loadHistory() {
    const data = await getHistory();
    setHistory(data);
    if (!latestImage && data.length > 0) setLatestImage(data[0]);
  }

  async function handleGenerate() {
    if (!prompt.trim()) return;
    setLoading(true);
    try {
      const image = await generateImage({ prompt, style });
      setLatestImage(image);
      setPrompt('');
      await loadHistory();
    } finally {
      setLoading(false);
    }
  }

  async function handleDelete(id: number) {
    await deleteHistoryItem(id);
    if (latestImage?.id === id) setLatestImage(null);
    await loadHistory();
  }

  useEffect(() => {
    loadHistory();
  }, []);

  return (
    <div className="appShell">
      <Header />

      <main>
        <section className="hero">
          <div>
            <p className="eyebrow">Full-stack AI platform foundation</p>
            <h2>Generate, enhance, store, and manage creative AI outputs.</h2>
            <p>
              VisionForge AI Part 1 gives you a professional React + FastAPI + SQLite foundation.
              The next parts add authentication, real AI generation, background jobs, and deployment.
            </p>
          </div>
          <div className="statsPanel">
            <div><strong>FastAPI</strong><span>Backend</span></div>
            <div><strong>React TS</strong><span>Frontend</span></div>
            <div><strong>SQLite</strong><span>Database</span></div>
          </div>
        </section>

        <section className="workspace">
          <CreatorPanel
            prompt={prompt}
            style={style}
            loading={loading}
            onPromptChange={setPrompt}
            onStyleChange={setStyle}
            onGenerate={handleGenerate}
          />
          <PreviewPanel image={latestImage} />
        </section>

        <HistoryGrid history={history} onDelete={handleDelete} />
      </main>
    </div>
  );
}

export default App;
