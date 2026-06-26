import { Trash2 } from 'lucide-react';
import type { ImageRecord } from '../types/image';

type Props = {
  history: ImageRecord[];
  onDelete: (id: number) => void;
};

export function HistoryGrid({ history, onDelete }: Props) {
  return (
    <section className="historySection">
      <div className="historyHeader">
        <div>
          <h2>Generation History</h2>
          <p>Saved locally in SQLite through the FastAPI backend.</p>
        </div>
        <span>{history.length} items</span>
      </div>

      {history.length === 0 ? (
        <div className="emptyHistory">No generations yet.</div>
      ) : (
        <div className="grid">
          {history.map((item) => (
            <article className="card" key={item.id}>
              <img src={item.image_url} alt={item.prompt} />
              <div className="cardBody">
                <div className="cardTop">
                  <span>{item.style}</span>
                  <button className="iconButton" onClick={() => onDelete(item.id)} aria-label="Delete image">
                    <Trash2 size={16} />
                  </button>
                </div>
                <h3>{item.prompt}</h3>
                <p>{item.enhanced_prompt}</p>
              </div>
            </article>
          ))}
        </div>
      )}
    </section>
  );
}
